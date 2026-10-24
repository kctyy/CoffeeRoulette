// Katy — main game screen: connects to the real-time game, shows questions, collects answers
import { useEffect, useRef, useState } from "react";
import { connectToGame, ServerEvent } from "../services/gameService";
import type { Question } from "../services/api";
import QuestionCard from "./QuestionCard";
import AnswerOptions from "./AnswerOptions";

export default function GameRoom({
  sessionId,
  userId,
  onGameOver,
}: {
  sessionId: string;
  userId: string;
  onGameOver: (scores: Record<string, number>, winner: string | null) => void;
}) {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [qIndex, setQIndex] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  const [opponentAnswered, setOpponentAnswered] = useState(false);
  const conn = useRef<ReturnType<typeof connectToGame> | null>(null);

  useEffect(() => {
    conn.current = connectToGame(sessionId, (e: ServerEvent) => {
      if (e.type === "game_start" || e.type === "next_round") {
        setQuestions(e.questions);
        setQIndex(0);
        setSelected(null);
      } else if (e.type === "opponent_answered") {
        setOpponentAnswered(true);
      } else if (e.type === "round_result") {
        // TODO: show correct answer + scores briefly, then advance
        setSelected(null);
        setOpponentAnswered(false);
        setQIndex((i) => i + 1);
      } else if (e.type === "game_over") {
        onGameOver(e.scores, e.winner);
      }
    });
    return () => conn.current?.close();
  }, [sessionId]);

  const question = questions[qIndex];
  if (!question) return <h2>Waiting for the game to start…</h2>;

  return (
    <div>
      <QuestionCard question={question} index={qIndex} total={questions.length} />
      <AnswerOptions
        options={question.options}
        selected={selected}
        disabled={selected !== null}
        onSelect={(i) => {
          setSelected(i);
          conn.current?.sendAnswer(question.id, i);
        }}
      />
      {opponentAnswered && <p>Your partner has answered ✅</p>}
    </div>
  );
}
