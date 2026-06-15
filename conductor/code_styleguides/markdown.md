# Markdown Style Guide

This document outlines the style guidelines for writing Markdown (`.md`) documentation in this project.

## 1. Structure and Headings
- **Single H1:** Each file must have exactly one H1 heading (`# Heading 1`) at the top representing the document title.
- **Hierarchy:** Maintain strict sequential hierarchy. Do not skip levels (e.g., do not follow `#` with `###`; use `##` first).
- **Capitalization:** Use Title Case for headings.

## 2. Formatting & Spacing
- **Blank Lines:** Insert exactly one blank line before and after all headings, lists, code blocks, and blockquotes.
- **Paragraphs:** Keep paragraphs short and concise. Keep line length wrapped naturally, or at 80-120 characters if using hard wrapping.
- **Emphasis:**
  - Use `**bold**` for strong emphasis or UI elements.
  - Use `*italics*` for key terms, citations, or file names.
  - Avoid overuse of formatting.

## 3. Lists
- **Consistency:** Use `-` for unordered lists.
- **Spacing:** For nested lists, use 2 or 4 spaces of indentation consistently.
- **Ending:** End list items with periods if they are complete sentences.

## 4. Code Blocks and Inline Code
- **Language Tags:** Always specify the programming language syntax tag on fenced code blocks (e.g., ```python, ```json, ```markdown).
- **Inline Code:** Use backticks `` `code` `` for code symbols, variable names, file paths, and terminal commands.

## 5. Callouts and Alerts
Use GitHub-style blockquote alerts strategically to highlight important information:
```markdown
> [!NOTE]
> Useful background context or info.

> [!IMPORTANT]
> Critical instructions or required constraints.

> [!WARNING]
> Warnings about breaking changes or potential pitfalls.
```
