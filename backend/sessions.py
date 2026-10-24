"""Create/join sessions, store mood check-ins, track game state."""
import uuid
from database import MEMORY
from matching import find_match
from models import JoinRequest, JoinResponse, Player, SessionInfo


def join_session(req: JoinRequest) -> JoinResponse:
    player = Player(user_id=req.user_id, display_name=req.display_name, mood=req.mood)
    MEMORY["checkins"][req.user_id] = req.mood  # TODO: persist to Supabase

    new_id = str(uuid.uuid4())[:8]
    match = find_match(new_id, player)

    if match is None:
        MEMORY["sessions"][new_id] = {"status": "waiting", "players": [player], "game_type": None}
        return JoinResponse(session_id=new_id, status="waiting")

    session_id, partner = match
    MEMORY["sessions"][session_id]["players"].append(player)
    MEMORY["sessions"][session_id]["status"] = "matched"
    return JoinResponse(session_id=session_id, status="matched", partner=partner)


def get_session(session_id: str) -> SessionInfo | None:
    s = MEMORY["sessions"].get(session_id)
    if not s:
        return None
    return SessionInfo(session_id=session_id, **s)
