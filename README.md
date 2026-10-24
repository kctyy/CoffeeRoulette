# CoffeeRoulette AI ☕🎲

Meet someone new, break the ice with an AI-directed game. Built for Cal Hacks — Meta track: *Bringing People Closer Together with AI*.

**Flow:** pick an emoji mood → get randomly matched → AI Game Director picks a game + generates questions → play together in real time → reconnect afterward.

Mock-up: https://www.figma.com/make/JsAZFY6DLyFpyiauq4hbn3/VibeCheck-Multiplayer-Game

## Team & ownership

| Area | Folder | Owner |
|---|---|---|
| Frontend – landing, mood, lobby, reconnect | `frontend/` | Sneha |
| Frontend – game room, questions, answers, results | `frontend/` | Katy |
| AI Game Director | `ai/` | Rena |
| Backend, matching, sessions, DB | `backend/` | Trisha |

API shapes live in [`docs/api-contract.md`](docs/api-contract.md). **Change the contract in a PR before changing code that depends on it.**

## Run it

Three terminals:

```bash
# 1. Backend (port 8000)
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in Supabase keys
uvicorn main:app --reload --port 8000

# 2. AI service (port 8001)
cd ai && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in LLM API key
uvicorn main:app --reload --port 8001

# 3. Frontend (port 5173)
cd frontend && npm install && npm run dev
```

The Vite dev server proxies `/api/*` → backend (8000) and `/ai/*` → AI service (8001), so the frontend never hardcodes ports.

## Git workflow

- `main` = always demo-able. Don't push broken code to it.
- One branch per person: `sneha/frontend`, `katy/game`, `rena/ai`, `trisha/backend`.
- Only edit files you own; if you need a change in someone else's file, message them or open a PR.
- Pull from `main` often.
