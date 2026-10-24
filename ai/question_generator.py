"""Generate game questions with the LLM."""
import uuid
from models import Question, Difficulty, GameType


# TODO (Rena): replace with a real LLM call that returns structured JSON.
def generate_questions(
    game_type: GameType,
    moods: list[str],
    difficulty: Difficulty,
    count: int,
    previous_questions: list[str],
) -> list[Question]:
    return [
        Question(
            id=str(uuid.uuid4())[:8],
            text=f"Placeholder question {i + 1} ({game_type})",
            options=["Option A", "Option B", "Option C", "Option D"],
            correct_index=0 if game_type == "trivia" else None,
            difficulty=difficulty,
        )
        for i in range(count)
    ]
