import random
from datetime import datetime

AGENTS = ["MCP-Tech", "MCP-Design"]

MCP_CONFIG = {
    "MCP-Tech": {
        "OBJECTIVE": "Gérer les tâches techniques",
        "STYLE": "sérieux et synthétique",
        "TASKS": [
            "Corriger les bugs critiques",
            "Mettre à jour l’API REST",
            "Configurer CI/CD GitHub Actions",
        ],
    },
    "MCP-Design": {
        "OBJECTIVE": "Superviser le design visuel",
        "STYLE": "créatif et amical",
        "TASKS": [
            "Créer une nouvelle maquette mobile",
            "Harmoniser les couleurs",
            "Préparer les visuels marketing",
        ],
    },
}

logs = []

def simulate_agent(agent_key):
    config = MCP_CONFIG[agent_key]
    task = random.choice(config["TASKS"])
    response = f"Tâche : {task} — Résolue avec succès."
    log = {
        "Agent": agent_key,
        "Tâche": task,
        "Réponse": response,
        "Heure": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Style": config["STYLE"],
    }
    logs.append(log)
    print(
        f"\n[{agent_key}] 🎯 {config['OBJECTIVE']}\n"
        f"🛠 Tâche : {task}\n"
        f"✅ {response}"
    )
    return log
