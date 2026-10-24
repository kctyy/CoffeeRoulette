// Sneha
export default function LandingPage({ onStart }: { onStart: () => void }) {
  return (
    <div>
      <h1>☕🎲 CoffeeRoulette</h1>
      <p>Meet someone new. Let AI pick the icebreaker.</p>
      <button onClick={onStart}>Get started</button>
    </div>
  );
}
