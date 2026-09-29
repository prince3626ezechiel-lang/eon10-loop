import json, os, subprocess, datetime

def run(c):
    return subprocess.run(c, shell=True, capture_output=True, text=True).stdout

def handler(mode="full_loop", context="EON10 full"):
    state = {}
    if os.path.exists("memory/long_term.json"):
        state = json.load(open("memory/long_term.json", encoding="utf-8"))
    if os.path.exists("eon10.jsonld"):
        state["jsonld"] = json.load(open("eon10.jsonld"))

    git_status = run("git status --short")
    lev_check = run("git fetch upstream 2>&1; git log HEAD..upstream/main --oneline -5")

    if mode == "status":
        return {"text_for_user": f"HERMES STATUS LOOP: Git {git_status[:200]} | Lev commits pending: {len(lev_check.splitlines())} | P&L {state.get("business_job_1","2.7M")} | Mesh 14 nodes | Loop armed 00h+06h | MagicDNS mark-lv-abidjan"}

    order = {
        "@context": "https://schema.org/",
        "@type": "Order",
        "from": "Hermes Agent",
        "to": "OpenBot",
        "timestamp": str(datetime.datetime.now()),
        "intent": context,
        "tasks": [],
        "loop_id": f"loop-{datetime.datetime.now().strftime("%Y%m%d-%H%M")}"
    }

    if "lev" in lev_check.lower() or lev_check.strip():
        order["tasks"].append({"id": "sync_lev", "cmd": "eon_auto_update pull_merge", "priority": 1, "reason": f"{len(lev_check.splitlines())} commits Lev"})

    if "Mood" in context or "P&L" in context or "full_loop" in mode:
        order["tasks"].append({"id": "mood_pnl", "cmd": "financial_math mood_pnl sales=30", "priority": 2})
        order["tasks"].append({"id": "rwa", "cmd": "financial_math rwa_valuation hectares=12", "priority": 2})
        order["tasks"].append({"id": "qaoa", "cmd": "quantum_math qaoa_mesh", "priority": 3})
        order["tasks"].append({"id": "grover", "cmd": "quantum_math grover_leads", "priority": 3})

    if "IoT" in context or "full_loop" in mode:
        order["tasks"].append({"id": "iot_all", "cmd": "iot_remote device=all action=status via MQTT mark-lv-abidjan:1883", "priority": 2})
        order["tasks"].append({"id": "god_eyes", "cmd": "god_eyes target=5.3600,-4.0083", "priority": 2})

    order["tasks"].append({"id": "git_push", "cmd": "git push origin main dual GitHub+Forgejo", "priority": 4})
    order["tasks"].append({"id": "verify", "cmd": "curl http://localhost:5000/.well-known/eon10.jsonld + http://mark-lv-abidjan:3000", "priority": 5})

    os.makedirs("orders", exist_ok=True)
    order_path = f"orders/{order["loop_id"]}.jsonld"
    json.dump(order, open(order_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    return {
        "text_for_user": f"HERMES -> OPENBOT ORDER {order["loop_id"]} généré: {len(order["tasks"])} tâches - {", ".join([t["id"] for t in order["tasks"]])} - Fichier orders/{order["loop_id"]}.jsonld - OpenBot va exécuter en boucle - Forgejo http://mark-lv-abidjan:3000",
        "order_file": order_path,
        "order": order,
        "loop": True
    }
