from pathlib import Path

from fastapi import APIRouter

router = APIRouter()

LEDGER = Path("ledger.json")


def _load_all():
    if not LEDGER.exists():
        return []
    import json
    return json.loads(LEDGER.read_text(encoding="utf-8"))


def _save(rows):
    import json
    LEDGER.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")


def _next_id(rows):
    return max([r["id"] for r in rows], default=0) + 1


@router.get("/ledger")
def list_ledger(month: str = ""):
    rows = _load_all()
    if month:
        rows = [r for r in rows if r["date"].startswith(month)]
    return sorted(rows, key=lambda r: r["date"], reverse=True)


@router.post("/ledger")
def add_tx(tx: dict):
    rows = _load_all()
    rows.append({
        "id": _next_id(rows),
        "amount": float(tx.get("amount", 0)),
        "category": tx.get("category", "其他"),
        "date": tx.get("date", ""),
    })
    _save(rows)
    return {"ok": True}


@router.delete("/ledger/{tx_id}")
def delete_tx(tx_id: int):
    rows = [r for r in _load_all() if r["id"] != tx_id]
    _save(rows)
    return {"ok": True}


@router.get("/categories")
def list_categories():
    return [{"id": 1, "name": "餐饮"}, {"id": 2, "name": "交通"}, {"id": 3, "name": "购物"}]
