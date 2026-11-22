"""持圭台（CHIGUITAI）· 人端交互，初审待圭笺

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：人端交互，初审待圭笺。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Chiguitai:
    """持圭台（CHIGUITAI）算子骨架 v0。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "CHIGUITAI"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

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
        """呈笺待人端执圭初审（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("CHIGUITAI.pending_review 骨架桩，候进化轮补齐")

    def human_verdict(self, verdict):
        """录入人端裁决，回传玄圭（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("CHIGUITAI.human_verdict 骨架桩，候进化轮补齐")
