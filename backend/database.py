"""Supabase client + helpers. Falls back to in-memory dicts if no keys are set."""
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = None
if SUPABASE_URL and SUPABASE_KEY:
    from supabase import create_client
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# In-memory fallback so everyone can develop before Supabase is set up.
MEMORY: dict[str, dict] = {"sessions": {}, "checkins": {}}

# TODO (Trisha): tables -> sessions, players, mood_checkins, answers, reconnects
