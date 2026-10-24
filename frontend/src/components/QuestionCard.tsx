// Katy — shows the current question text + round progress
import type { Question } from "../services/api";

export default function QuestionCard({ question, index, total }: { question: Question; index: number; total: number }) {
  return (
    <div>
      <small>Question {index + 1} of {total}</small>
      <h2>{question.text}</h2>
    </div>
  );
}
