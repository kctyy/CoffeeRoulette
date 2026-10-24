// Katy — answer buttons
export default function AnswerOptions({
  options,
  selected,
  disabled,
  onSelect,
}: {
  options: string[];
  selected: number | null;
  disabled: boolean;
  onSelect: (index: number) => void;
}) {
  return (
    <div style={{ display: "grid", gap: 8 }}>
      {options.map((opt, i) => (
        <button
          key={i}
          disabled={disabled}
          onClick={() => onSelect(i)}
          style={{ background: selected === i ? "#ffe9b0" : "white" }}
        >
          {opt}
        </button>
      ))}
    </div>
  );
}
