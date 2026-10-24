from typing import Literal, Optional
from pydantic import BaseModel

Difficulty = Literal["easy", "medium", "hard"]
GameType = Literal["trivia", "would_you_rather", "two_truths_one_lie", "this_or_that"]


class Question(BaseModel):
    id: str
    text: str
    options: list[str]
    correct_index: Optional[int] = None
    difficulty: Difficulty = "medium"


class RecommendGameRequest(BaseModel):
    moods: list[str]


class RecommendGameResponse(BaseModel):
    game_type: GameType
    reason: str


class GenerateQuestionsRequest(BaseModel):
    game_type: GameType
    moods: list[str]
    difficulty: Difficulty = "medium"
    count: int = 5
    previous_questions: list[str] = []


class GenerateQuestionsResponse(BaseModel):
    questions: list[Question]


class AdaptDifficultyRequest(BaseModel):
    scores: dict[str, int]
    current_difficulty: Difficulty
    round: int


class AdaptDifficultyResponse(BaseModel):
    difficulty: Difficulty
    reason: str
