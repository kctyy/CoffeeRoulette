// Sneha
const MOODS = ["😊", "😴", "🔥", "😌", "🤪", "😅"];

export default function MoodCheckIn({ onSelect }: { onSelect: (mood: string) => void }) {
  return (
    <div>
      <h2>How are you feeling?</h2>
      <div style={{ display: "flex", gap: 12, flexWrap: "wrap", fontSize: "2rem" }}>
        {MOODS.map((m) => (
          <button key={m} onClick={() => onSelect(m)} style={{ fontSize: "2rem" }}>{m}</button>
        ))}
      </div>
    </div>
  );
}
