// KaTeX auto-render for MkDocs Material (instant navigation compatible)
document$.subscribe(function () {
  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true },
    ],
    throwOnError: false,
    trust: true,
    macros: {
      "\\R": "\\mathbb{R}",
      "\\N": "\\mathbb{N}",
    },
  });
});
