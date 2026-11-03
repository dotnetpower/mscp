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
    trust: false,
    errorCallback: function (message, error) {
      console.error("MSCP math rendering failed:", message, error);
    },
    macros: {
      "\\R": "\\mathbb{R}",
      "\\N": "\\mathbb{N}",
    },
  });
});
