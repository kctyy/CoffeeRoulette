// Sneha — post-game "stay connected?" screen
export default function Reconnect({ onChoose }: { onChoose: (wants: boolean) => void }) {
  return (
    <div>
      <h2>Want to keep chatting?</h2>
      <button onClick={() => onChoose(true)}>Yes, reconnect ☕</button>{" "}
      <button onClick={() => onChoose(false)}>No thanks</button>
    </div>
  );
}
