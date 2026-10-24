from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from models import JoinRequest, JoinResponse, SessionInfo, AnswerRequest, ReconnectRequest, ReconnectResponse
from sessions import join_session, get_session

app = FastAPI(title="CoffeeRoulette Backend")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# session_id -> connected websockets
connections: dict[str, list[WebSocket]] = {}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/sessions/join", response_model=JoinResponse)
def join(req: JoinRequest):
    return join_session(req)


@app.get("/api/sessions/{session_id}", response_model=SessionInfo)
def session(session_id: str):
    s = get_session(session_id)
    if not s:
        raise HTTPException(404, "Session not found")
    return s


@app.post("/api/sessions/{session_id}/answer")
def answer(session_id: str, req: AnswerRequest):
    # TODO: store answer, broadcast `opponent_answered`, score the round when both answered
    return {"accepted": True}


@app.post("/api/sessions/{session_id}/reconnect", response_model=ReconnectResponse)
def reconnect(session_id: str, req: ReconnectRequest):
    # TODO: if both wants_reconnect -> create meeting link via integrations/meeting_bot.py
    return ReconnectResponse(mutual=False, meeting_link=None)


@app.websocket("/api/ws/{session_id}")
async def ws(websocket: WebSocket, session_id: str):
    await websocket.accept()
    connections.setdefault(session_id, []).append(websocket)
    try:
        while True:
            msg = await websocket.receive_json()
            # TODO: handle {"type": "answer", ...}; broadcast events from docs/api-contract.md
            for conn in connections[session_id]:
                if conn is not websocket:
                    await conn.send_json(msg)
    except WebSocketDisconnect:
        connections[session_id].remove(websocket)
