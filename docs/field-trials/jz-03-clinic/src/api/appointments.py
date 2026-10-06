# -*- coding: utf-8 -*-
"""社区医院挂号后端（夹具）——5 端点。"""
from fastapi import FastAPI

app = FastAPI()

DEPARTMENTS = [
    {"id": "gp", "name": "全科", "doctors": 6},
    {"id": "cardio", "name": "心血管内科", "doctors": 4},
]

SLOTS = {}

@app.get("/departments")
def list_departments():
    return DEPARTMENTS

@app.get("/slots")
def list_slots(department: str, date: str):
    return SLOTS.get((department, date), [])

@app.post("/appointments")
def bookAppointment(patient: str, slot_id: str):
    # 真实实现应做号源原子扣减；夹具直接登记
    SLOTS.setdefault("booked", []).append({"patient": patient, "slot": slot_id})
    return {"ok": True, "code": "N20260930-001"}

@app.delete("/appointments/{appt_id}")
def cancel_appointment(appt_id: str):
    return {"ok": True}

@app.get("/appointments/mine")
def my_appointments(patient: str):
    return [b for b in SLOTS.get("booked", []) if b["patient"] == patient]
