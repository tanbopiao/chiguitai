"""持圭台（CHIGUITAI）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
import unittest

from chiguitai import Chiguitai


class TestChiguitai(unittest.TestCase):
    def setUp(self):
        self.op = Chiguitai()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "chiguitai")
        self.assertEqual(d["code"], "CHIGUITAI")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_pending_review_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.pending_review(None)

    def test_human_verdict_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.human_verdict(None)


if __name__ == "__main__":
    unittest.main()
