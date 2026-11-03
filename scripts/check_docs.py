"""Check built public documentation without fetching or reading private sources."""

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
import math
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]

PLA_ZERO_CALL_EQUATION = r"\operatorname{LLMCalls}(\tau_{\mathrm{PLA}})=0"
PLA_PIPELINE_EDGES = (
    {
        ("EXT", "PARSE"),
        ("PARSE", "TYPE"),
        ("TYPE", "SEM"),
        ("TYPE", "REJECT"),
        ("SEM", "CHECK"),
        ("CHECK", "STORE"),
        ("CHECK", "REJECT"),
        ("REJECT", "WAIT"),
    },
    {
        ("TRIG", "CTX"),
        ("CTX", "PLAN"),
        ("PLAN", "COMPOSE"),
        ("COMPOSE", "REALIZE"),
        ("REALIZE", "VALID"),
        ("VALID", "EMIT"),
        ("VALID", "HOLD"),
        ("HOLD", "PLAN"),
        ("HOLD", "STOP"),
    },
)


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.equations = []
        self.diagrams = []
        self.article = False
        self._math = None
        self._math_tag = None
        self._diagram = None
        self._diagram_tag = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if "md-content__inner" in classes:
            self.article = True
        if "arithmatex" in classes:
            if self._math is not None:
                raise ValueError(f"{self.path}: nested math wrapper")
            self._math = []
            self._math_tag = tag
        if "mermaid" in classes:
            if self._diagram is not None:
                raise ValueError(f"{self.path}: nested Mermaid wrapper")
            self._diagram = []
            self._diagram_tag = tag

    def handle_data(self, data):
        if self._math is not None:
            self._math.append(data)
        if self._diagram is not None:
            self._diagram.append(data)

    def handle_endtag(self, tag):
        if self._math is not None and tag == self._math_tag:
            value = "".join(self._math).strip()
            display = self._math_tag == "div"
            left, right = ("\\[", "\\]") if display else ("\\(", "\\)")
            if not (value.startswith(left) and value.endswith(right)):
                raise ValueError(f"{self.path}: invalid math delimiters: {value[:80]}")
            self.equations.append((value[2:-2], display))
            self._math = None
            self._math_tag = None
        if self._diagram is not None and tag == self._diagram_tag:
            self.diagrams.append("".join(self._diagram).strip())
            self._diagram = None
            self._diagram_tag = None


def normalize_equation(value):
    # Text labels are localized; compare the surrounding mathematical structure.
    pattern = re.compile(r"\\text(?:it|bf|rm)?\{")
    while match := pattern.search(value):
        end = match.end()
        depth = 1
        while end < len(value) and depth:
            if value[end] == "{":
                depth += 1
            elif value[end] == "}":
                depth -= 1
            end += 1
        if depth:
            raise ValueError("Unclosed text label in equation")
        value = value[: match.start()] + value[end:]
    value = re.sub(r"\\(?:left|right|qquad|quad)\b|\\[,!;:]", "", value)
    return re.sub(r"\s+", "", value)


def check_links(pages, site):
    errors = []
    checked = 0
    for path, page in pages.items():
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            checked += 1
            relative = unquote(url.path)
            if relative.startswith("/"):
                relative = re.sub(r"^/mscp(?:/|$)", "/", relative)
                target = site / relative.lstrip("/")
            else:
                target = path.parent / relative if relative else path
            target = target.resolve()
            if not target.is_relative_to(site):
                errors.append(f"{path.relative_to(site)}: link leaves the built site: {href}")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{path.relative_to(site)}: missing link target: {href}")
            elif url.fragment and target.suffix == ".html":
                fragment = unquote(url.fragment)
                target_page = pages.get(target)
                if target_page is None or fragment not in target_page.ids:
                    errors.append(f"{path.relative_to(site)}: missing fragment: {href}")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"Local links: {checked} checked, 0 errors")


def check_bilingual_contracts(pages, site):
    contracts = {
        "MSCP_Overview": ("\\psi(M_T)", "|R(t+1)-R(t)|"),
        "specs/Why_LLM_Free_PLA": ("\\operatorname{LLMCalls}", "\\operatorname{Realize}"),
        "levels/Level_4_5_Self_Architecting": ("\\text{detect drift}",),
        "levels/Level_4_8_Strategic_Self_Modeling": ("B\\gamma",),
        "levels/Level_5_Proto_AGI": ("T_{\\max}",),
    }
    checked = 0
    for stem, markers in contracts.items():
        english = pages[site / stem / "index.html"]
        korean = pages[site / "ko" / stem / "index.html"]
        for marker in markers:
            expected = Counter(
                normalize_equation(value)
                for value, display in english.equations
                if display and marker in value
            )
            actual = Counter(
                normalize_equation(value)
                for value, display in korean.equations
                if display and marker in value
            )
            if not expected or actual != expected:
                raise ValueError(f"Bilingual contract mismatch: {stem}: {marker}")
            checked += sum(expected.values())
    print(f"Bilingual critical equations: {checked} matched")


def check_pla_contract(pages, site):
    edge_pattern = re.compile(r"\s*([A-Z][A-Z0-9_]*)\s*-->\s*(?:\|[^|\n]*\|)?\s*([A-Z][A-Z0-9_]*)\s*")
    for locale in ("", "ko"):
        path = site / locale / "specs/Why_LLM_Free_PLA/index.html"
        if path not in pages:
            raise ValueError(f"{path}: PLA documentation page missing")
        page = pages[path]
        equations = {normalize_equation(value) for value, display in page.equations if display}
        if normalize_equation(PLA_ZERO_CALL_EQUATION) not in equations:
            raise ValueError(f"{path}: PLA zero-LLM contract missing")
        if len(page.diagrams) != len(PLA_PIPELINE_EDGES):
            raise ValueError(f"{path}: expected two PLA pipeline diagrams")
        for index, (diagram, expected) in enumerate(zip(page.diagrams, PLA_PIPELINE_EDGES), 1):
            if re.search(r"\bLLM[PS]\b|\bLLM\s*\(\s*producer|\bre-prompt\b", diagram, re.I):
                raise ValueError(f"{path}: LLM producer or fallback in PLA diagram {index}")
            declared = set(re.findall(r"^\s*([A-Z][A-Z0-9_]*)\s*[\[{]", diagram, re.M))
            expected_nodes = {node for edge in expected for node in edge}
            actual = []
            for line in diagram.splitlines():
                if "-->" not in line:
                    continue
                match = edge_pattern.fullmatch(line)
                if match is None:
                    raise ValueError(f"{path}: unsupported PLA edge syntax in diagram {index}")
                actual.append(match.groups())
            if declared != expected_nodes or set(actual) != expected or len(actual) != len(expected):
                raise ValueError(f"{path}: PLA pipeline structure changed in diagram {index}")
    print("PLA documentation: zero-LLM contract and both pipeline structures verified in English and Korean")


def check_numerical_regressions():
    def entropy(values):
        return -sum(p * math.log2(p) for p in values if p > 0)
    p, q = (0.9, 0.1), (0.1, 0.9)
    if not math.isclose(entropy(p), entropy(q)) or p == q:
        raise ValueError("Equal-entropy counterexample failed")
    midpoint = tuple((a + b) / 2 for a, b in zip(p, q))
    divergence = entropy(midpoint) - (entropy(p) + entropy(q)) / 2
    if not 0 < divergence <= 1:
        raise ValueError("Jensen-Shannon diagnostic regression failed")

    def resilience(cognition, recovery):
        return min(1, cognition / 0.30) * 500 / max(500, recovery)

    for cognition in (0, 0.15, 0.30, 0.60, 1):
        scores = [resilience(cognition, t) for t in (0, 1, 250, 500, 1000)]
        if not all(0 <= score <= 1 for score in scores):
            raise ValueError("Resilience score outside [0, 1]")
        if scores != sorted(scores, reverse=True):
            raise ValueError("Slower recovery incorrectly improves resilience")
    if not resilience(0.15, 0) < resilience(0.30, 0) == 1:
        raise ValueError("Below-baseline cognition must reduce resilience")
    future = sum(0.95**k for k in range(1, 11))
    bound = 0.95 * (1 - 0.95**10) / (1 - 0.95)
    if not future > 0 or not math.isclose(future, bound):
        raise ValueError("Zero-immediate-reward EVR regression failed")

    required = {
        "levels/Level_5_Proto_AGI": (
            r"\min\left\{1,\frac{C_{\min}(s)}{MVC}\right\}",
            r"\frac{T_{\max}}{\max\{T_{\max},T_{\text{recover}}(s)\}}",
        ),
        "levels/Level_4_8_Strategic_Self_Modeling": (
            r"\frac{B\gamma(1-\gamma^H)}{1-\gamma}",
        ),
    }
    for stem, snippets in required.items():
        for suffix in (".md", ".ko.md"):
            text = (ROOT / "docs" / (stem + suffix)).read_text(encoding="utf-8")
            text = text.replace("\\left", "").replace("\\right", "")
            for snippet in snippets:
                snippet = snippet.replace("\\left", "").replace("\\right", "")
                if re.sub(r"\s+", "", snippet) not in re.sub(r"\s+", "", text):
                    raise ValueError(f"Corrected equation missing: {stem}{suffix}")
    print("Numerical regressions: entropy counterexample, resilience bounds/direction/zero time, EVR bound passed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=ROOT / "site")
    site = parser.parse_args().site_dir.resolve()
    if not site.is_dir():
        raise ValueError("Build the documentation first: mkdocs build --strict")
    pages = {}
    items = []
    for path in sorted(site.rglob("*.html")):
        page = Page(path)
        page.feed(path.read_text(encoding="utf-8"))
        if page._math is not None:
            raise ValueError(f"{path}: unclosed math wrapper")
        if page._diagram is not None:
            raise ValueError(f"{path}: unclosed Mermaid wrapper")
        if page.article:
            pages[path] = page
            for index, (value, display) in enumerate(page.equations, 1):
                items.append({
                    "file": str(path.relative_to(site)),
                    "index": index,
                    "math": value,
                    "display": display,
                })
    if not pages:
        raise ValueError("No generated documentation pages found")
    check_links(pages, site)
    check_bilingual_contracts(pages, site)
    check_pla_contract(pages, site)
    check_numerical_regressions()
    subprocess.run(
        ["node", str(ROOT / "scripts/check-math.cjs")],
        input=json.dumps(items),
        text=True,
        cwd=ROOT,
        check=True,
    )
    sources = [p for p in (ROOT / "docs").rglob("*.md") if ".ko." not in p.name]
    definitions = sum(
        len(re.findall(r"\*\*Definition \d+(?:\.\d+)? \(", p.read_text(encoding="utf-8")))
        for p in sources
    )
    print(f"Documentation inventory: {len(sources)} English sources, {definitions} numbered definitions, {len(pages)} built pages")


if __name__ == "__main__":
    main()
