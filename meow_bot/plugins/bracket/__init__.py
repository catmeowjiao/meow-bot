from nonebot import on_message
from nonebot.params import EventPlainText
from nonebot.plugin import PluginMetadata
from nonebot.typing import T_State

__plugin_meta__ = PluginMetadata(
    name="括号补全",
    description="发送左括号自动补全右括号",
    usage='发送左括号自动补全右括号, 如发送"([", Bot会回复"])"\n注:"([)]"不被认为是匹配的括号, 因此发送"([)", Bot不会回复',
)

bracket_pairs = {
    "(": ")",
    "（": "）",
    "[": "]",
    "【": "】",
    "{": "}",
    "｛": "｝",
    "<": ">",
    "《": "》",
    "「": "」",
    "『": "』",
    "⁅": "⁆",
    "〈": "〉",
    "❬": "❭",
    "❰": "❱",
    "❲": "❳",
    "❴": "❵",
    "⟦": "⟧",
    "⟨": "⟩",
    "⟪": "⟫",
    "⟬": "⟭",
    "⦃": "⦄",
    "⦗": "⦘",
    "〈": "〉",
    "〔": "〕",
    "〖": "〗",
    "〘": "〙",
    "〚": "〛",
    "﹛": "﹜",
    "﹝": "﹞",
    "［": "］",
    "｢": "｣",
    "«": "»",
}


async def check_brackets(state: T_State, text: str = EventPlainText()):
    brackets = []
    for char in text:
        for open_bracket, close_bracket in bracket_pairs.items():
            if char == open_bracket:
                brackets.append(close_bracket)
                break
            elif char == close_bracket:
                if not brackets or brackets.pop() != close_bracket:
                    return False
    if not brackets:
        return False
    state["brackets"] = "".join(reversed(brackets))
    return True


bracket = on_message(check_brackets, priority=1, block=False)


@bracket.handle()
async def _(state: T_State):
    await bracket.finish(state["brackets"])
