import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_pdf_page_density import body_coverage


class LayoutDensityTests(unittest.TestCase):
    def test_sparse_page_is_below_threshold(self):
        words = [{"top": 50, "bottom": 220}]
        self.assertLess(body_coverage(words, 792), 0.60)

    def test_balanced_page_meets_threshold(self):
        words = [{"top": 50, "bottom": 710}]
        self.assertGreaterEqual(body_coverage(words, 792), 0.60)

    def test_footer_does_not_mask_sparse_content(self):
        words = [{"top": 50, "bottom": 220}, {"top": 760, "bottom": 770}]
        self.assertLess(body_coverage(words, 792), 0.60)


if __name__ == "__main__":
    unittest.main()
