# -*- coding: utf-8 -*-
"""订阅计费服务（夹具）——6 端点。"""
from fastapi import FastAPI

app = FastAPI()

SUB = {"plan": None, "status": "trialing"}
INVOICES = {}

@app.get("/plans")
def list_plans():
    return [{"id": "basic", "price": 9}, {"id": "pro", "price": 29}]

@app.post("/subscribe")
def subscribe(plan: str):
    SUB["plan"], SUB["status"] = plan, "active"
    return SUB

@app.post("/subscribe/upgrade")
def upgrade(plan: str):
    SUB["plan"] = plan
    return {"ok": True, "proration": 0}

@app.post("/subscription/cancel")
def cancel():
    SUB["status"] = "canceled"
    return {"ok": True, "effective": "period_end"}

@app.get("/invoices")
def list_invoices():
    return list(INVOICES.values())

@app.get("/invoices/{id}/download")
def download_invoice(id: str):
    return INVOICES.get(id, {})
