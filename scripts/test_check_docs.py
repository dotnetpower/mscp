import contextlib
from html import escape
import io
from pathlib import Path
import unittest

from check_docs import Page, PLA_PIPELINE_EDGES, PLA_ZERO_CALL_EQUATION, check_pla_contract


class PlaDocumentationTests(unittest.TestCase):
    def setUp(self):
        self.site = Path("/public-docs")
        self.pages = {}
        for locale in ("", "ko"):
            path = self.site / locale / "specs/Why_LLM_Free_PLA/index.html"
            page = Page(path)
            page.equations = [(PLA_ZERO_CALL_EQUATION, True)]
            for edges in PLA_PIPELINE_EDGES:
                nodes = sorted({node for edge in edges for node in edge})
                lines = ["flowchart TB"]
                lines.extend(f'{node}["{node}"]' for node in nodes)
                lines.extend(f"{source} --> {target}" for source, target in sorted(edges))
                page.diagrams.append("\n".join(lines))
            self.pages[path] = page
        self.english = self.pages[self.site / "specs/Why_LLM_Free_PLA/index.html"]
        self.korean = self.pages[self.site / "ko/specs/Why_LLM_Free_PLA/index.html"]

    def check(self):
        with contextlib.redirect_stdout(io.StringIO()):
            check_pla_contract(self.pages, self.site)

    def test_accepts_non_llm_pipelines_without_entropy_diagnostics(self):
        self.check()

    def test_parser_preserves_mermaid_source_and_arrow_labels(self):
        source = 'flowchart TB\nA["입력"]\nB["출력"]\nA -->|통과| B'
        page = Page(Path("page.html"))
        page.feed(f'<pre class="mermaid"><code>{escape(source)}</code></pre>')
        self.assertEqual(page.diagrams, [source])

    def test_rejects_missing_zero_call_contract(self):
        self.english.equations = []
        with self.assertRaisesRegex(ValueError, "zero-LLM contract missing"):
            self.check()

    def test_rejects_nonzero_call_contract(self):
        self.english.equations = [(PLA_ZERO_CALL_EQUATION.replace("=0", "=1"), True)]
        with self.assertRaisesRegex(ValueError, "zero-LLM contract missing"):
            self.check()

    def test_rejects_llm_generation_and_fallback_in_either_language(self):
        for page in (self.english, self.korean):
            for index in (0, 1):
                with self.subTest(page=page.path, diagram=index):
                    original = page.diagrams[index]
                    page.diagrams[index] += '\nLLMS["LLM (producer)"]\nREALIZE --> LLMS'
                    with self.assertRaisesRegex(ValueError, "LLM producer or fallback"):
                        self.check()
                    page.diagrams[index] = original

    def test_rejects_bypassed_realization(self):
        self.korean.diagrams[1] = self.korean.diagrams[1].replace(
            "COMPOSE --> REALIZE", "COMPOSE --> EMIT"
        )
        with self.assertRaisesRegex(ValueError, "pipeline structure changed"):
            self.check()

    def test_rejects_hidden_extra_dependency_node(self):
        self.english.diagrams[1] += '\nBACKEND["Undeclared backend"]'
        with self.assertRaisesRegex(ValueError, "pipeline structure changed"):
            self.check()

    def test_rejects_missing_pipeline(self):
        self.english.diagrams.pop()
        with self.assertRaisesRegex(ValueError, "expected two PLA pipeline diagrams"):
            self.check()


if __name__ == "__main__":
    unittest.main()
