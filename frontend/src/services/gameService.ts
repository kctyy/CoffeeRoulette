// Katy: real-time game connection (WebSocket events from docs/api-contract.md)
import type { Question } from "./api";

export type ServerEvent =
  | { type: "player_joined"; player: unknown }
  | { type: "game_start"; game_type: string; questions: Question[] }
  | { type: "opponent_answered"; user_id: string; question_id: string }
  | { type: "round_result"; question_id: string; correct_index?: number; answers: Record<string, number>; scores: Record<string, number> }
  | { type: "next_round"; questions: Question[]; difficulty: string }
  | { type: "game_over"; scores: Record<string, number>; winner: string | null };

export function connectToGame(sessionId: string, onEvent: (e: ServerEvent) => void) {
  const proto = location.protocol === "https:" ? "wss" : "ws";
  const ws = new WebSocket(`${proto}://${location.host}/api/ws/${sessionId}`);

  ws.onmessage = (msg) => onEvent(JSON.parse(msg.data) as ServerEvent);

  return {
    sendAnswer: (question_id: string, answer_index: number) =>
      ws.send(JSON.stringify({ type: "answer", question_id, answer_index })),
    close: () => ws.close(),
  };
}
