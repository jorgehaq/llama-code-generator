import json
from pathlib import Path

def load_ollama_config(path="config/ollama-config.json"):
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"⚠️ Config file not found: {path}")
    
    with open(config_path) as f:
        cfg = json.load(f)

    return cfg

if __name__ == "__main__":
    config = load_ollama_config()
    print("✅ Loaded config:")
    for key, val in config.items():
        print(f"  {key}: {val}")