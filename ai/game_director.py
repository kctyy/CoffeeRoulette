"""Orchestrates mood analysis, question generation, and difficulty adaptation."""
from mood_analyzer import recommend_game
from question_generator import generate_questions
from difficulty_adapter import adapt_difficulty

__all__ = ["recommend_game", "generate_questions", "adapt_difficulty"]
