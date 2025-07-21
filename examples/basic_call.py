import requests
import json
from pathlib import Path
import time

def load_config():
    config_path = Path("config/ollama-config.json")
    if not config_path.exists():
        raise FileNotFoundError("❌ Configuration file not found.")
    
    with open(config_path) as f:
        return json.load(f)

def query_ollama(prompt, config):
    url = config.get("api_base_url", "http://localhost:11434") + "/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": config.get("default_model", "llama2"),
        "prompt": prompt,
        "stream": config.get("streaming", False),
        "options": {
            "temperature": config.get("temperature", 0.7),
            "top_p": config.get("top_p", 0.95),
            "num_predict": config.get("max_tokens", 2048)
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), stream=data["stream"])
        response.raise_for_status()

        if data["stream"]:
            full_response = ""
            for line in response.iter_lines():
                if line:
                    partial = json.loads(line.decode("utf-8"))
                    if "response" in partial:
                        print(partial["response"], end="", flush=True)
                        full_response += partial["response"]
            print()  # newline after stream output
            return {"response": full_response}

        else:
            return response.json()

    except Exception as e:
        print("❌ Error while querying Ollama:", e)
        return None

if __name__ == "__main__":
    cfg = load_config()
    prompt = "Donde queda la ciudad de Bucaramanga?"
    start_time = time.time()
    result = query_ollama(prompt, cfg)
    end_time = time.time()

    if result and "response" in result:
        print(f"\n🧠 Solicitud: {prompt} \n")
        print("\n🧠 LLAMA2 Response:\n")
        print(result["response"])
        print(f"\n⏱️ Total response time: {end_time - start_time:.2f} seconds")
    else:
        print("⚠️ No valid response received.")
