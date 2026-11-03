const assert = require("node:assert/strict");
const fs = require("node:fs");
const katex = require("katex");

const options = {
  throwOnError: true,
  strict: "error",
  trust: false,
  macros: { "\\R": "\\mathbb{R}", "\\N": "\\mathbb{N}" },
};

assert.throws(() => katex.renderToString("\\undefinedMSCPCommand", options));
katex.renderToString("\\text{권한, 불변식, 비가역성, 위험 정책 실패}", options);

const config = fs.readFileSync("mkdocs.yml", "utf8");
const versions = [...config.matchAll(/katex@([\d.]+)\//g)].map((match) => match[1]);
assert.equal(versions.length, 3, "Expected the three configured KaTeX assets");
assert.ok(versions.every((version) => version === katex.version), "KaTeX asset and checker versions differ");

const items = JSON.parse(fs.readFileSync(0, "utf8"));
assert.ok(items.length > 0, "No rendered math was found");
let failures = 0;
for (const item of items) {
  try {
    katex.renderToString(item.math, { ...options, displayMode: item.display });
  } catch (error) {
    failures += 1;
    console.error(`${item.file}: math item ${item.index}: ${error.message}`);
  }
}
console.log(`KaTeX ${katex.version}: ${items.length} math items, ${failures} errors`);
process.exitCode = failures === 0 ? 0 : 1;
