import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from claim_validator import validate_claims

class EvidenceValidationTests(unittest.TestCase):
    def test_exact_match_is_allowed(self):
        self.assertEqual([], validate_claims({"technology": {"PostgreSQL"}}, {"technology": {"PostgreSQL"}}))

    def test_partial_match_does_not_become_exact_technology(self):
        findings = validate_claims({"technology": {"PostgreSQL"}}, {"technology": {"MySQL"}})
        self.assertEqual("technology", findings[0].kind)

    def test_missing_evidence_is_flagged(self):
        findings = validate_claims({}, {"responsibility": {"Built REST APIs"}})
        self.assertEqual("responsibility", findings[0].kind)

    def test_experience_duration_requirement_needs_explicit_support(self):
        findings = validate_claims({"year": {"2025"}}, {"year": {"2 years of professional experience"}})
        self.assertEqual("year", findings[0].kind)

    def test_hallucinated_metrics_and_skills_are_flagged(self):
        findings = validate_claims({"skill": {"JavaScript"}}, {"skill": {"JavaScript", "Node.js"}, "metric": {"reduced costs by 30%"}})
        self.assertEqual({"skill", "metric"}, {item.kind for item in findings})

if __name__ == "__main__":
    unittest.main()
