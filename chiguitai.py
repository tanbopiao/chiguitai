"""持圭台（CHIGUITAI）· 人端交互，初审待圭笺

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：人端交互，初审待圭笺。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Chiguitai:
    """持圭台（CHIGUITAI）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "CHIGUITAI"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.queue = []
        self.verdicts = []
        self._seq = 0

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "chiguitai",
            "cn": "持圭台",
            "code": self.CODE,
            "duty": "人端交互，初审待圭笺",
            "mingwen": "人端执圭，初审呈笺",
            "anchor": self.ANCHOR,
        }

    def pending_review(self, jiancao):
        """呈笺待人端执圭初审。"""
        self._seq += 1
        ticket = "CGT-%04d" % self._seq
        self.queue.append({"ticket": ticket, "jiancao": jiancao, "status": "pending"})
        self.events.append({"event": "pending_review", "ticket": ticket})
        return ticket

    def human_verdict(self, verdict):
        """录入人端裁决，回传玄圭。"""
        if not self.queue:
            raise RuntimeError("无待审笺稿")
        item = self.queue.pop(0)
        item["status"] = "adjudicated"
        record = {"ticket": item["ticket"], "verdict": verdict, "forwarded_to": "xuangui"}
        self.verdicts.append(record)
        self.events.append({"event": "human_verdict", "ticket": item["ticket"], "verdict": verdict})
        return record
