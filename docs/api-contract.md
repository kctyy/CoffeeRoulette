# API Contract

Single source of truth between frontend, backend, and AI. Edit here first, then code.

- **Backend** (Trisha): `http://localhost:8000` — frontend calls `/api/...`
- **AI service** (Rena): `http://localhost:8001` — frontend/backend call `/ai/...`

## Shared types

```ts
type Mood = "😊" | "😴" | "🔥" | "😌" | "🤪" | "😅";   // extend as needed
type Difficulty = "easy" | "medium" | "hard";
type GameType = "trivia" | "would_you_rather" | "two_truths_one_lie" | "this_or_that";

interface Question {
  id: string;
  text: string;
  options: string[];          // answer choices
  correct_index?: number;     // omit for opinion-style games
  difficulty: Difficulty;
}
```

## Backend (Trisha)

### `POST /api/sessions/join`
Join the matching queue with a mood check-in.
```json
// request
{ "user_id": "u_123", "display_name": "Katy", "mood": "😊" }
// response
{ "session_id": "s_abc", "status": "waiting" | "matched", "partner": { "user_id": "u_456", "display_name": "Sam", "mood": "🔥" } | null }
```

### `GET /api/sessions/{session_id}`
```json
{ "session_id": "s_abc", "status": "waiting" | "matched" | "playing" | "finished",
  "players": [{ "user_id": "u_123", "display_name": "Katy", "mood": "😊" }, ...],
  "game_type": "trivia" | null }
```

### `POST /api/sessions/{session_id}/answer`
```json
// request
{ "user_id": "u_123", "question_id": "q1", "answer_index": 2 }
// response
{ "accepted": true }
```

### `POST /api/sessions/{session_id}/reconnect`
Both players opt in to stay connected after the game.
```json
// request
{ "user_id": "u_123", "wants_reconnect": true }
// response
{ "mutual": true, "meeting_link": "https://meet.google.com/..." | null }
```

### Real-time: `WS /api/ws/{session_id}`
Server → client events (JSON, `type` field):
| type | payload |
|---|---|
| `player_joined` | `{ player }` |
| `game_start` | `{ game_type, questions: Question[] }` |
| `opponent_answered` | `{ user_id, question_id }` |
| `round_result` | `{ question_id, correct_index?, answers: {user_id: index}, scores: {user_id: n} }` |
| `next_round` | `{ questions: Question[], difficulty }` |
| `game_over` | `{ scores: {user_id: n}, winner: user_id \| null }` |

Client → server: `{ "type": "answer", "question_id": "q1", "answer_index": 2 }`

## AI service (Rena)

### `POST /ai/recommend-game`
```json
// request
{ "moods": ["😊", "🔥"] }
// response
{ "game_type": "trivia", "reason": "Both energetic — go competitive!" }
```

### `POST /ai/generate-questions`
```json
// request
{ "game_type": "trivia", "moods": ["😊", "🔥"], "difficulty": "medium", "count": 5, "previous_questions": [] }
// response
{ "questions": [Question, ...] }
```

### `POST /ai/adapt-difficulty`
```json
// request
{ "scores": { "u_123": 3, "u_456": 1 }, "current_difficulty": "medium", "round": 2 }
// response
{ "difficulty": "easy" | "medium" | "hard", "reason": "..." }
```
