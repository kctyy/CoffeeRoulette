"""Random matching: pair waiting players."""
import random
from models import Player

waiting_queue: list[tuple[str, Player]] = []  # (session_id, player)


def find_match(session_id: str, player: Player) -> tuple[str, Player] | None:
    """Return (existing_session_id, partner) if someone is waiting, else queue this player."""
    if waiting_queue:
        idx = random.randrange(len(waiting_queue))
        return waiting_queue.pop(idx)
    waiting_queue.append((session_id, player))
    return None
