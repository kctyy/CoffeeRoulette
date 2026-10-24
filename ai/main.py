from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from game_director import recommend_game, generate_questions, adapt_difficulty
from models import (
    RecommendGameRequest, RecommendGameResponse,
    GenerateQuestionsRequest, GenerateQuestionsResponse,
    AdaptDifficultyRequest, AdaptDifficultyResponse,
)

load_dotenv()
app = FastAPI(title="CoffeeRoulette AI Game Director")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ai/recommend-game", response_model=RecommendGameResponse)
def recommend(req: RecommendGameRequest):
    game_type, reason = recommend_game(req.moods)
    return RecommendGameResponse(game_type=game_type, reason=reason)


@app.post("/ai/generate-questions", response_model=GenerateQuestionsResponse)
def questions(req: GenerateQuestionsRequest):
    qs = generate_questions(req.game_type, req.moods, req.difficulty, req.count, req.previous_questions)
    return GenerateQuestionsResponse(questions=qs)


@app.post("/ai/adapt-difficulty", response_model=AdaptDifficultyResponse)
def adapt(req: AdaptDifficultyRequest):
    difficulty, reason = adapt_difficulty(req.scores, req.current_difficulty, req.round)
    return AdaptDifficultyResponse(difficulty=difficulty, reason=reason)
