"""持圭台（CHIGUITAI）算子单测：名帖完整、行为达标、只增不覆盖。"""
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

    def test_pending_review(self):
        ticket = self.op.pending_review("笺稿一")
        self.assertTrue(ticket.startswith("CGT-"))

    def test_human_verdict(self):
        self.op.pending_review("笺稿一")
        record = self.op.human_verdict("allow")
        self.assertEqual(record["forwarded_to"], "xuangui")
        with self.assertRaises(RuntimeError):
            self.op.human_verdict("deny")


if __name__ == "__main__":
    unittest.main()
