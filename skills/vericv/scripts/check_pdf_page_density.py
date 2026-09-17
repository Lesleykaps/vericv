"""Flag unusually sparse PDF pages so CV layouts are reviewed before delivery."""
from __future__ import annotations

import argparse
from pathlib import Path

import pdfplumber


def body_coverage(words: list[dict], page_height: float, margin: float = 36.0) -> float:
    """Return the vertical share of the printable body occupied by extracted words."""
    # Ignore headers and footers: a page number must not make a sparse page pass.
    body_words = [
        word for word in words
        if word["top"] >= margin and word["bottom"] <= page_height - margin
    ]
    if not body_words:
        return 0.0
    top = min(word["top"] for word in body_words)
    bottom = max(word["bottom"] for word in body_words)
    printable_height = page_height - (2 * margin)
    return max(0.0, bottom - top) / printable_height


def inspect_pdf(path: Path, minimum_body_coverage: float = 0.60) -> list[tuple[int, float]]:
    """Return (page number, coverage) for pages whose text occupies too little height."""
    warnings: list[tuple[int, float]] = []
    with pdfplumber.open(path) as pdf:
        for index, page in enumerate(pdf.pages, start=1):
            coverage = body_coverage(page.extract_words(), page.height)
            if coverage < minimum_body_coverage:
                warnings.append((index, coverage))
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--minimum-body-coverage", type=float, default=0.60)
    args = parser.parse_args()
    warnings = inspect_pdf(args.pdf, args.minimum_body_coverage)
    if not warnings:
        print("PDF page-density check passed")
        return 0
    for page, coverage in warnings:
        print(f"Page {page}: sparse body coverage ({coverage:.0%}); inspect and rebalance the CV.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
