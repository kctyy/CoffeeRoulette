// Shared API calls + types. Keep in sync with docs/api-contract.md

export type Mood = string; // emoji
export type Difficulty = "easy" | "medium" | "hard";
export type GameType = "trivia" | "would_you_rather" | "two_truths_one_lie" | "this_or_that";

export interface Player {
  user_id: string;
  display_name: string;
  mood: Mood;
}

export interface Question {
  id: string;
  text: string;
  options: string[];
  correct_index?: number;
  difficulty: Difficulty;
}

export interface JoinResponse {
  session_id: string;
  status: "waiting" | "matched";
  partner: Player | null;
}

async function post<T>(url: string, body: unknown): Promise<T> {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`${url} failed: ${res.status}`);
  return res.json();
}

async function get<T>(url: string): Promise<T> {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${url} failed: ${res.status}`);
  return res.json();
}

export const api = {
  joinSession: (user_id: string, display_name: string, mood: Mood) =>
    post<JoinResponse>("/api/sessions/join", { user_id, display_name, mood }),

  getSession: (session_id: string) => get<any>(`/api/sessions/${session_id}`),

  submitAnswer: (session_id: string, user_id: string, question_id: string, answer_index: number) =>
    post<{ accepted: boolean }>(`/api/sessions/${session_id}/answer`, { user_id, question_id, answer_index }),

  reconnect: (session_id: string, user_id: string, wants_reconnect: boolean) =>
    post<{ mutual: boolean; meeting_link: string | null }>(`/api/sessions/${session_id}/reconnect`, {
      user_id,
      wants_reconnect,
    }),
};
