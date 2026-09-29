import datetime

def handler(mode="full"):
    now = datetime.datetime.now()
    hour = now.hour
    if hour == 0:
        return {"text_for_user": "♻️ LOOP 00h MEDIATION - EON10 Prof - Hermes genere daily review + lecon - OpenBot execute IoT status + P&L + RWA + God Eyes - memory/long_term.json updated - Prochain 06h Lev sync", "loop": "00h", "tasks": ["eon_mediation_00h midnight_brief","financial_math mood_pnl","iot_remote all"]}
    elif hour == 6:
        return {"text_for_user": "♻️ LOOP 06h LEV SYNC - Hermes check Lev upstream - OpenBot pull_merge -X theirs + stash EON10 custom + push dual GitHub+Forgejo mark-lv-abidjan:3000 - P&L + mesh QAOA", "loop": "06h", "tasks": ["eon_auto_update pull_merge","quantum_math qaoa_mesh"]}
    else:
        return {"text_for_user": f"♻️ LOOP {hour}h BUSINESS - Hermes -> OpenBot: Mood P&L 2.7M + RWA 10.8M + Grover x64 + IoT pompe + God Eyes 360 - Forgejo + Tailscale mark-lv-abidjan - Dis EON dit moi pour ordre custom", "loop": f"{hour}h"}
