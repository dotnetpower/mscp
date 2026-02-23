// KaTeX auto-render for MkDocs Material
document.addEventListener("DOMContentLoaded", function () {
  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
    ],
    throwOnError: false,
    // Trust all KaTeX commands used in MSCP docs
    trust: true,
    // Macros used across the documentation
    macros: {
      "\\R": "\\mathbb{R}",
      "\\N": "\\mathbb{N}",
    },
  });
});
