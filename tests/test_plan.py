import unittest

from oif_cognitive.plan import validate_plan


class PlanTests(unittest.TestCase):
    def test_valid_dependency_chain(self):
        plan = {"steps": [{"id": "a", "depends_on": []}, {"id": "b", "depends_on": ["a"]}]}
        self.assertEqual(validate_plan(plan), [])

    def test_unknown_dependency(self):
        plan = {"steps": [{"id": "a", "depends_on": ["missing"]}]}
        self.assertTrue(any("unknown step" in e for e in validate_plan(plan)))

    def test_cycle(self):
        plan = {"steps": [{"id": "a", "depends_on": ["b"]}, {"id": "b", "depends_on": ["a"]}]}
        self.assertTrue(any("cycle" in e for e in validate_plan(plan)))

    def test_supported_conclusion_requires_evidence(self):
        plan = {"steps": [], "conclusions": [{"id": "c", "status": "supported", "evidence_ids": []}]}
        self.assertTrue(any("lacks evidence" in e for e in validate_plan(plan)))


if __name__ == "__main__":
    unittest.main()
