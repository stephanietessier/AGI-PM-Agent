import os
import sys

# Ensure the project root is on the path for imports when pytest runs as a script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import agipm_agent


def test_simulate_agent_single_log():
    # Ensure logs is empty before running
    agipm_agent.logs.clear()
    agipm_agent.simulate_agent("MCP-Tech")
    assert len(agipm_agent.logs) == 1
    assert {"Agent", "Tâche", "Réponse", "Heure", "Style"} <= agipm_agent.logs[0].keys()
