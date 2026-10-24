// Sneha — top-level screen flow
import { useState } from "react";
import LandingPage from "./components/LandingPage";
import MoodCheckIn from "./components/MoodCheckIn";
import Lobby from "./components/Lobby";
import GameRoom from "./components/GameRoom";
import GameResults from "./components/GameResults";
import Reconnect from "./components/Reconnect";
import { api } from "./services/api";

type Screen = "landing" | "mood" | "lobby" | "game" | "results" | "reconnect" | "done";

// Temp user identity until real auth exists
const userId = "u_" + Math.random().toString(36).slice(2, 8);

export default function App() {
  const [screen, setScreen] = useState<Screen>("landing");
  const [sessionId, setSessionId] = useState("");
  const [lobbyStatus, setLobbyStatus] = useState<"waiting" | "matched">("waiting");
  const [result, setResult] = useState<{ scores: Record<string, number>; winner: string | null }>({ scores: {}, winner: null });

  async function handleMood(mood: string) {
    setScreen("lobby");
    const res = await api.joinSession(userId, "Guest", mood);
    setSessionId(res.session_id);
    setLobbyStatus(res.status);
    // TODO: poll/subscribe until matched, then setScreen("game")
    if (res.status === "matched") setScreen("game");
  }

  return (
    <>
      {screen === "landing" && <LandingPage onStart={() => setScreen("mood")} />}
      {screen === "mood" && <MoodCheckIn onSelect={handleMood} />}
      {screen === "lobby" && <Lobby status={lobbyStatus} />}
      {screen === "game" && (
        <GameRoom
          sessionId={sessionId}
          userId={userId}
          onGameOver={(scores, winner) => { setResult({ scores, winner }); setScreen("results"); }}
        />
      )}
      {screen === "results" && (
        <GameResults scores={result.scores} winner={result.winner} userId={userId} onContinue={() => setScreen("reconnect")} />
      )}
      {screen === "reconnect" && (
        <Reconnect onChoose={async (wants) => { await api.reconnect(sessionId, userId, wants); setScreen("done"); }} />
      )}
      {screen === "done" && <h2>Thanks for playing! ☕</h2>}
    </>
  );
}
