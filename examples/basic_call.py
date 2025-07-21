import requests
import json

def query_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    prompt = "What is FastAPI in Python?"
    result = query_ollama(prompt)
    print("\n🧠 RESPONSE FROM LLAMA2:")
    print(result["response"])