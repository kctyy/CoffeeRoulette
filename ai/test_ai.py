from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_recommend_game():
    r = client.post("/ai/recommend-game", json={"moods": ["😊", "🔥"]})
    assert r.status_code == 200
    assert "game_type" in r.json()


def test_generate_questions():
    r = client.post("/ai/generate-questions", json={
        "game_type": "trivia", "moods": ["😊", "🔥"], "difficulty": "medium", "count": 3,
    })
    assert r.status_code == 200
    assert len(r.json()["questions"]) == 3


def test_adapt_difficulty():
    r = client.post("/ai/adapt-difficulty", json={
        "scores": {"a": 5, "b": 1}, "current_difficulty": "hard", "round": 2,
    })
    assert r.json()["difficulty"] == "medium"
