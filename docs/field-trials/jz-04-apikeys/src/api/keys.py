# -*- coding: utf-8 -*-
"""开放平台密钥服务（夹具）——4 端点。明文只在创建响应返回一次，库里只落哈希。"""
from fastapi import FastAPI

app = FastAPI()

KEYS = {}

@app.post("/keys")
def create_key(name: str):
    key_id = "k_" + name
    KEYS[key_id] = {"name": name, "status": "active", "hash": "sha256:..."}
    # 明文占位：真实实现返回随机值一次；夹具不落任何真实密钥
    return {"id": key_id, "plaintext": "<once-only-placeholder>"}

@app.get("/keys")
def list_keys():
    return [{"id": k, "fingerprint": v["hash"][:12], "status": v["status"]} for k, v in KEYS.items()]

@app.delete("/keys/{key_id}")
def revoke_key(key_id: str):
    KEYS[key_id]["status"] = "revoked"
    return {"ok": True}

@app.get("/keys/{key_id}/usage")
def key_usage(key_id: str):
    return {"calls_24h": 0, "errors_24h": 0}
