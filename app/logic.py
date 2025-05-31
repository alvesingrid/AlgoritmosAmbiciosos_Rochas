from typing import List
from app.models import Event

def interval_scheduling(events: List[Event]) -> List[Event]:
    # Ordena os eventos pelo horário de término
    sorted_events = sorted(events, key=lambda e: e.end)
    scheduled = []
    current_end = None

    for event in sorted_events:
        if current_end is None or event.start >= current_end:
            scheduled.append(event)
            current_end = event.end

    return scheduled

