<!--
Copyright (c) 2026 Moon Hyuk Choi
Licensed under the MIT License.
See LICENSE file in the repository root for full license information.

Redistribution (commercial or non-commercial) must retain this notice.
Removal of attribution constitutes a license violation.
-->
# MSCP Project — Copilot Instructions

## 1. Language

- All documentation and code **must be written in English only**.

## 2. Project Scope & Disclaimer

- This is a **personal research project** and does **not** represent any official position of any organization or company.
- **MSCP (Minimal Self-Consciousness Protocol)** is the core protocol of the AGI engine explored in this repository.
- This repository covers concepts **up to and including Level 5** only. Content that goes **beyond Level 5** must **never** be mentioned, referenced, or implied in any form.

## 3. Repository Boundaries

- The actual project implementation lives at `~/dev/agent-san`. This repository (`mscp`) is solely for **conceptual documentation**.
- Only files under the `docs/` folder should be referenced or modified.
- **No implementation details, source code, configuration, or any specifics of the actual project (`agent-san`) may be included in this repository.** The focus must remain strictly on MSCP concept formalization.

## 4. Academic Rigor

- Every term, theory, and mechanism **must** include rigorous mathematical notation with detailed explanations.
- Use LaTeX-compatible notation (KaTeX for Markdown rendering):
  - Inline math: `$...$`
  - Block math: `$$...$$`
- All content must meet **publication-grade quality** (peer-review-ready level of precision and clarity).

## 5. Error-Free Guarantee — Mandatory Correction Loop

When writing or modifying any content, the following loop **must** be executed:

```
REPEAT:
  1. Write or modify content
  2. Verify for errors (factual, mathematical, logical, grammatical, structural)
  3. IF error_count > 0 → Correct all errors → GOTO 1
  4. IF error_count == 0 → DONE
```

This loop runs **indefinitely** until zero errors remain. There is no shortcut or early exit.

## 6. Diagrams

- When a concept requires a visual diagram, **do not create it inline**.
- Instead, leave a `<!-- TODO: [description] -->` marker at the location in the document.
- Record the same item in `docs/TODO.md` with sufficient context for later creation.

## 7. Change Tracking via TODO.md

- Every content update (new section, revision, correction, structural change) **must** be logged in `docs/TODO.md`.
- Format each entry with:
  - Date (`YYYY-MM-DD`)
  - File affected
  - Brief description of the change or pending work
- `TODO.md` serves as the single source of truth for outstanding and completed work.

## 8. Reference Scope

- Only reference documents within the `docs/` folder of this repository.
- Do not link to or depend on external URLs, private repositories, or implementation artifacts.

## 9. Domain-Neutral Language

- All examples, scenarios, and illustrations **must use domain-neutral, universally understandable terms**.
- **Avoid** business-specific, industry-specific, or context-dependent terminology such as: *partnership*, *contract*, *vendor*, *client engagement*, *SLA*, etc.
- **Prefer** generic terms: *project*, *task*, *product*, *item*, *resource*, *service*, *system*, etc.
- This rule ensures that documentation remains accessible to readers from any background and does not imply affiliation with any specific business domain.

## 10. KaTeX Compatibility Rules

All math notation must render correctly in **GitHub-flavored Markdown with KaTeX**. The following rules are mandatory:

### 10.1 Forbidden Commands
- **`\textunderscore{}`** — Not supported in KaTeX. Never use it.
- **`\_` inside `\text{}` or `\textit{}`** — Underscores are illegal in KaTeX text mode.
- **`\textbf{}` with underscores** — Same restriction applies.

### 10.2 Identifier Naming in Math Mode
When a mathematical variable or function name contains multiple words (e.g., `identity_volatility`):

| Context | Correct | Wrong |
|---------|---------|-------|
| Subscript | `V_{\text{identity}}` | `V_{identity\_volatility}` |
| Multi-word subscript | `\hat{\delta}_{\text{goal weight}}` | `\hat{\delta}_{goal\_weight}` |
| Function name | `\text{mention count}(e)` | `\text{mention\_count}(e)` |
| Italic identifier | `\textit{core value vector}` | `\textit{core\_value\_vector}` |
| `\operatorname` | `\operatorname{MSI}(t)` | (preferred for function-like names) |

**Rule**: Use **spaces** instead of underscores inside `\text{}`, `\textit{}`, and `\textbf{}`. For subscripts, wrap in `\text{}` to stay in text mode: `X_{\text{my label}}`.

### 10.3 Pipe Characters (`|`) Inside Markdown Tables

Markdown uses `|` as a **column separator**. When a KaTeX expression containing `|` is placed inside a table cell, the parser breaks the cell boundary. This applies to **all** uses of `|` in math — absolute value, cardinality, norms, set-builder notation, etc.

| Context | Correct | Wrong |
|---------|---------|-------|
| Cardinality | `$\lvert\mathcal{T}\rvert$` | `$\|\mathcal{T}\|$` or `$\mid\mathcal{T}\mid$` |
| Absolute value | `$\lvert x \rvert$` | `$\|x\|$` |
| Norm | `$\lVert v \rVert_2$` | `$\|v\|_2$` |
| Set notation | `$\lbrace x \rbrace$` | `$\{x\}$` (may also break) |

**Rule**: Inside markdown tables, **always** use `\lvert`/`\rvert` (single bar) or `\lVert`/`\rVert` (double bar) instead of `|`, `\|`, or `\mid`. Use `\lbrace`/`\rbrace` instead of `\{`/`\}`.

> Outside tables (blockquotes, standalone `$$` blocks), bare `|` and `\{`/`\}` are safe.

### 10.4 Underscore Emphasis Conflict in Tables

When a single `$...$` inline math block inside a markdown table cell contains **two or more `_` characters**, the markdown parser pairs them as emphasis markers (`_..._` = italic), stripping the underscores before KaTeX processes the expression. This completely breaks math rendering.

**Fix**: Escape subscript underscores with `\_` inside table-cell math. GitHub markdown consumes the `\` (preventing emphasis) and passes a clean `_` to KaTeX.

| Context | Correct (in table) | Wrong (in table) |
|---------|---------|-------|
| Two subscripts | `$\mathcal{P}\_{T^{\ast}} \to \mathcal{D}\_{T^{\ast}}$` | `$\mathcal{P}_{T^*} \to \mathcal{D}_{T^*}$` |
| Three subscripts | `$V\_{id} + M\_{goal} + \sigma^2\_{pred}$` | `$V_{id} + M_{goal} + \sigma^2_{pred}$` |
| Single subscript | `$\mathcal{P}_{T^{\ast}}$` (safe — only one `_`) | — |

**Rule**: Inside markdown tables, if a single `$...$` block contains **2+ subscript `_`**, escape each as `\_`. A single `_` per `$...$` block is safe and does not need escaping.

> Outside tables, bare `_` subscripts are always safe regardless of count.

### 10.5 Asterisk Emphasis Conflict in Tables

The same emphasis problem applies to `*`. When a single `$...$` block inside a table cell contains **two or more `*` characters** (e.g., `T^*` appearing twice), the markdown parser treats them as italic markers (`*...*`), stripping the asterisks before KaTeX processes the expression.

**Fix**: Replace bare `*` with the KaTeX command `\ast` inside table-cell math when there are 2+ asterisks in one `$...$` block.

| Context | Correct (in table) | Wrong (in table) |
|---------|---------|-------|
| Two asterisks | `$\mathcal{P}\_{T^{\ast}} \to \mathcal{D}\_{T^{\ast}}$` | `$\mathcal{P}\_{T^*} \to \mathcal{D}\_{T^*}$` |
| Single asterisk | `$\mathcal{P}_{T^*}$` (safe — only one `*`) | — |

**Rule**: Inside markdown tables, if a single `$...$` block contains **2+ literal `*`**, replace each with `\ast`. A single `*` per `$...$` block is safe.

> Outside tables, bare `*` in math is always safe regardless of count.

### 10.6 Safe Patterns
- Plain math subscripts with single letters: `x_i`, `C_t`, `w_1` — always safe.
- `\text{}` for multi-character subscripts: `R_{\text{post}}` — safe.
- `\operatorname{}` for function names: `\operatorname{CDTS}` — safe.
- `\mathrm{}` for upright multi-letter names: `\mathrm{SHA}` — safe.

### 10.7 Pre-Commit Check
Before finalizing any math block, mentally verify:
1. No raw `_` appears inside `\text{}`, `\textit{}`, or `\textbf{}`.
2. No `\textunderscore` appears anywhere.
3. All multi-word identifiers use spaces (not underscores) in text-mode commands.
4. All `$$...$$` blocks have blank lines before and after them (required for GitHub rendering).
5. No bare `|`, `\|`, or `\{`/`\}` appear in math expressions **inside markdown tables**.
6. No single `$...$` block inside a table cell has 2+ unescaped `_` (use `\_` instead).
7. No single `$...$` block inside a table cell has 2+ bare `*` (use `\ast` instead).
