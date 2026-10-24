from typing import Literal, Optional
from pydantic import BaseModel


class Player(BaseModel):
    user_id: str
    display_name: str
    mood: str


class JoinRequest(BaseModel):
    user_id: str
    display_name: str
    mood: str


class JoinResponse(BaseModel):
    session_id: str
    status: Literal["waiting", "matched"]
    partner: Optional[Player] = None


class SessionInfo(BaseModel):
    session_id: str
    status: Literal["waiting", "matched", "playing", "finished"]
    players: list[Player]
    game_type: Optional[str] = None


class AnswerRequest(BaseModel):
    user_id: str
    question_id: str
    answer_index: int


class ReconnectRequest(BaseModel):
    user_id: str
    wants_reconnect: bool


class ReconnectResponse(BaseModel):
    mutual: bool
    meeting_link: Optional[str] = None
