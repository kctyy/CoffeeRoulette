"""Rules for making the next round easier/harder based on scores."""
from models import Difficulty

ORDER: list[Difficulty] = ["easy", "medium", "hard"]


def adapt_difficulty(scores: dict[str, int], current: Difficulty, round_num: int) -> tuple[Difficulty, str]:
    if len(scores) < 2:
        return current, "Not enough players to adapt."
    values = sorted(scores.values(), reverse=True)
    gap = values[0] - values[1]
    idx = ORDER.index(current)
    if gap >= 3 and idx > 0:
        return ORDER[idx - 1], "One player is far ahead — easing up so it stays fun."
    if gap == 0 and idx < len(ORDER) - 1:
        return ORDER[idx + 1], "Tied game — turning up the heat."
    return current, "Keeping difficulty the same."
