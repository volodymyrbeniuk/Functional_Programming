"""Capstone: pure log filtering and aggregation."""
from dataclasses import dataclass
from typing import Iterable
@dataclass(frozen=True)
class Event: level:str; message:str; duration_ms:int

def parse_line(line:str) -> Event:
    parts=line.split("|",2)
    if len(parts)!=3: raise ValueError(f"invalid log line: {line!r}")
    level,message,duration=parts
    try: ms=int(duration)
    except ValueError as exc: raise ValueError("duration must be an integer") from exc
    if ms<0: raise ValueError("duration must be non-negative")
    return Event(level.strip().upper(),message.strip(),ms)
def filter_events(events:Iterable[Event],level:str="ERROR") -> list[Event]: return [event for event in events if event.level==level.upper()]
def total_duration(events:Iterable[Event]) -> int: return sum(event.duration_ms for event in events)
def summarize(events:Iterable[Event]) -> dict[str,object]:
    rows=list(events); errors=filter_events(rows)
    return {"count":len(rows),"errors":len(errors),"total_duration_ms":total_duration(rows),"messages":[e.message for e in errors]}
def main() -> None:
    events=[parse_line("INFO|ready|3"),parse_line("ERROR|disk full|18")]; print(summarize(events))
if __name__=="__main__": main()
