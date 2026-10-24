// Sneha — waiting for a match
export default function Lobby({ status }: { status: "waiting" | "matched" }) {
  return (
    <div>
      <h2>{status === "waiting" ? "Finding your match…" : "Matched! Starting game…"}</h2>
    </div>
  );
}
