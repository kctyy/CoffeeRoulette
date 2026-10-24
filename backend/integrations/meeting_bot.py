"""Pick a provider and create a meeting link when both players want to reconnect."""
from integrations import google_meet, zoom


def create_meeting_link(provider: str = "google_meet") -> str:
    if provider == "zoom":
        return zoom.create_meeting()
    return google_meet.create_meeting()
