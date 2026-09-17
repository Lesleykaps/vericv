# Tailored CV layout quality

Read this when producing a CV document or PDF.

## Page budget

Use the candidate's content and the requested format to choose the page count. A requested maximum is not a requirement to pad; when the user requests an exact count, use the available, relevant evidence to make each page useful and visually balanced.

- Do not insert a manual page break until the CV has been fully structured and the natural flow has been assessed.
- For a two-page CV, distribute supported sections deliberately. Put the most job-relevant experience and skills first, then use selected projects, education, and other relevant documented evidence to make the second page substantive.
- Do not create vague filler, repeat skills, enlarge headings excessively, add decorative elements, or invent content to fill space.
- Do not shrink margins below 0.5 inch or reduce body text below 9 pt merely to force content into a target page count.
- If the supplied evidence cannot truthfully sustain the requested count without a conspicuously sparse page, ask whether the user wants a shorter CV or can provide additional documented material.

## Render-and-balance gate

After generating the file, render every page and inspect it at normal reading size. A page is suspect when a large blank area is caused by a manual page break or by holding relevant content for a later sparse page.

Revise in this order:

1. Remove unnecessary manual page breaks and let the content flow naturally.
2. Reorder or move supported, job-relevant projects, education details, and evidence-bearing bullets to balance pages.
3. Restore a readable type size and natural spacing rather than compressing or padding.
4. If the exact page count remains unprofessional, disclose the conflict and recommend the truthful shorter version.

For a generated PDF, run `scripts/check_pdf_page_density.py <file.pdf>` after visual review. Its warning is a prompt to inspect and rebalance, not a substitute for judgment: short final pages can be appropriate only when no useful supported content can be moved there.
