# 🌐 Ollama API Examples

This file shows sample API calls you can use to query local models via Ollama's REST API.

## 🧠 Basic Prompt (curl)

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Explain what is FastAPI in Python",
  "stream": false
}'
```

  ## 🧪 JSON Request Format

```json
{
  "model": "llama2",
  "prompt": "Your prompt here",
  "stream": false
}
``

## 🔁 Streaming Response (experimental)

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Generate a Python function",
  "stream": true
}'
```

## 🔍 List Installed Models

```bash
curl http://localhost:11434/api/tags
```

## 📥 Available Models

```bash
ollama list
```

Use `ollama pull <model>` to download more.

