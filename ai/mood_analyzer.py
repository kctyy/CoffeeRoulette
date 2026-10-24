"""Turn two players' emoji moods into a game recommendation."""
from models import GameType

# Rule-based fallback so the demo still works if the LLM is down.
ENERGETIC = {"🔥", "🤪", "😊"}


def fallback_game_for_moods(moods: list[str]) -> tuple[GameType, str]:
    energetic = sum(m in ENERGETIC for m in moods)
    if energetic == len(moods):
        return "trivia", "You're both feeling energetic — go competitive!"
    if energetic == 0:
        return "this_or_that", "Low-key vibes — an easy, chill game."
    return "would_you_rather", "Mixed energy — a conversation starter fits best."


# TODO (Rena): call the LLM with both moods and return (game_type, reason).
def recommend_game(moods: list[str]) -> tuple[GameType, str]:
    return fallback_game_for_moods(moods)
