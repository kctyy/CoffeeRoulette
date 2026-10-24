// Katy — end-of-game scores
export default function GameResults({
  scores,
  winner,
  userId,
  onContinue,
}: {
  scores: Record<string, number>;
  winner: string | null;
  userId: string;
  onContinue: () => void;
}) {
  return (
    <div>
      <h2>{winner === null ? "It's a tie! 🤝" : winner === userId ? "You won! 🎉" : "Nice try! 👏"}</h2>
      <ul>
        {Object.entries(scores).map(([id, s]) => (
          <li key={id}>{id === userId ? "You" : "Partner"}: {s}</li>
        ))}
      </ul>
      <button onClick={onContinue}>Continue</button>
    </div>
  );
}
