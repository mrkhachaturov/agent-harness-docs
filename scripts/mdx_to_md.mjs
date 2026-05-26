#!/usr/bin/env node
// MDX → Markdown converter for opencode docs.
//
// Reads MDX from stdin, emits clean Markdown on stdout. Used by
// fetch_opencode_docs.py one file at a time.
//
// What it strips:
//   - `import` / `export` statements (mdxjsEsm nodes)
//   - JSX expression containers (e.g. `{config.console}`) — replaced with empty text
//
// What it preserves:
//   - All standard markdown (headings, lists, code blocks, links, tables)
//   - Frontmatter (passed through untouched via remark-frontmatter? — actually
//     Starlight frontmatter we keep manually; see below)
//   - Starlight directive callouts (`:::tip`, `:::note`) — left as-is because
//     they're valid markdown directives that downstream tools handle.
//
// How it handles JSX components:
//   - Unwraps the component, keeping its children. So
//       <Card title="X">body</Card>
//     becomes just `body`. Attribute info is lost — that's fine for an
//     index/search use case. For specific Starlight wrappers we add small
//     hints (Tabs → sequential sections, Steps → ordered list).

import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkMdx from "remark-mdx";
import remarkGfm from "remark-gfm";
import remarkStringify from "remark-stringify";
import { visit, SKIP } from "unist-util-visit";
import { toString as mdastToString } from "mdast-util-to-string";

function readStdin() {
  return new Promise((resolve, reject) => {
    let data = "";
    process.stdin.setEncoding("utf8");
    process.stdin.on("data", (chunk) => (data += chunk));
    process.stdin.on("end", () => resolve(data));
    process.stdin.on("error", reject);
  });
}

// Strip MDX-only nodes (imports/exports, JSX expressions) and unwrap JSX
// element nodes while keeping their children.
function stripMdx() {
  return (tree) => {
    visit(tree, (node, index, parent) => {
      if (!parent || index == null) return;

      // Drop top-level `import` / `export` blocks and bare JS expressions.
      if (
        node.type === "mdxjsEsm" ||
        node.type === "mdxFlowExpression" ||
        node.type === "mdxTextExpression"
      ) {
        parent.children.splice(index, 1);
        return [SKIP, index];
      }

      // Unwrap JSX components, replacing the node with its children.
      if (
        node.type === "mdxJsxFlowElement" ||
        node.type === "mdxJsxTextElement"
      ) {
        const children = node.children || [];

        // For purely text-bearing inline elements with no children we drop them.
        if (children.length === 0) {
          parent.children.splice(index, 1);
          return [SKIP, index];
        }

        // For <Tabs><TabItem label="X">...</TabItem></Tabs>:
        //   each TabItem becomes a small heading + its children, so the
        //   distinct tabs are preserved as readable sections.
        if (node.name === "Tabs") {
          const expanded = [];
          for (const child of children) {
            if (child.type === "mdxJsxFlowElement" && child.name === "TabItem") {
              const label = (child.attributes || []).find(
                (a) => a.name === "label" || a.name === "value",
              );
              if (label && typeof label.value === "string") {
                expanded.push({
                  type: "paragraph",
                  children: [{ type: "strong", children: [{ type: "text", value: label.value }] }],
                });
              }
              expanded.push(...(child.children || []));
            } else {
              expanded.push(child);
            }
          }
          parent.children.splice(index, 1, ...expanded);
          return [SKIP, index];
        }

        // Default: replace the JSX element with its children in place.
        parent.children.splice(index, 1, ...children);
        return [SKIP, index];
      }
    });
  };
}

// Strip any remaining JSX attributes residue inside text (paranoia, after unwrap).
function pruneEmptyParagraphs() {
  return (tree) => {
    visit(tree, "paragraph", (node, index, parent) => {
      if (!parent || index == null) return;
      const text = mdastToString(node).trim();
      if (text === "") {
        parent.children.splice(index, 1);
        return [SKIP, index];
      }
    });
  };
}

async function main() {
  const input = await readStdin();
  if (!input.trim()) {
    process.stdout.write("");
    return;
  }

  // Preserve frontmatter manually: remark-mdx parsing strips unknown leading
  // YAML if not paired with remark-frontmatter. We extract it, then re-emit.
  let frontmatter = "";
  let body = input;
  const fmMatch = input.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
  if (fmMatch) {
    frontmatter = fmMatch[0];
    body = input.slice(fmMatch[0].length);
  }

  const file = await unified()
    .use(remarkParse)
    .use(remarkMdx)
    .use(remarkGfm)
    .use(stripMdx)
    .use(pruneEmptyParagraphs)
    .use(remarkStringify, {
      bullet: "-",
      fences: true,
      listItemIndent: "one",
      rule: "-",
      ruleRepetition: 3,
      ruleSpaces: false,
    })
    .process(body);

  process.stdout.write(frontmatter + String(file));
}

main().catch((err) => {
  process.stderr.write(`mdx_to_md error: ${err.stack || err.message}\n`);
  process.exit(1);
});
