"""Pure CSV/JSON transformations with IO isolated at the edges."""
import csv, json
from pathlib import Path
from typing import Iterable

def normalize(rows: Iterable[dict[str,str]]) -> list[dict[str,object]]:
    result=[]
    for row in rows:
        try: amount=float(row["amount"])
        except (KeyError,ValueError) as exc: raise ValueError(f"invalid amount in row {row!r}") from exc
        if amount<0: raise ValueError("amount must be non-negative")
        result.append({"category":row.get("category","").strip().lower(),"amount":round(amount,2)})
    return result

def read_csv(path: Path) -> list[dict[str,str]]:
    with path.open(newline="",encoding="utf-8") as source: return list(csv.DictReader(source))
def write_json(path: Path, rows: list[dict[str,object]]) -> None:
    path.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf-8")
def run(input_path: Path, output_path: Path) -> None: write_json(output_path,normalize(read_csv(input_path)))
def main() -> None:
    sample=[{"category":" Food ","amount":"12.5"}]; print(normalize(sample))
if __name__=="__main__": main()
