# 🧠 Setup Guide – Local Ollama AI Environment

This guide explains how to install and run the Ollama AI server locally to power language model inference (like llama2) on your own machine.

## ✅ Prerequisites

- Ubuntu Linux (VM or host)
- At least 8GB RAM, 10GB disk
- Python 3.10+ and `venv`
- Git installed

## 📦 Installation

Run the installer script:

```bash
./scripts/install-ollama.sh
```

This will install Ollama to `/usr/local/bin/ollama`.

## ⬇️ Download Model

Use the provided helper script:

```bash
./models/download-models.sh
```

Default model: `llama2`

## 🚀 Start Ollama Server

Launch in background:

```bash
./scripts/start-ollama.sh
```

Server will run at:  
`http://localhost:11434`

## 🔍 Test the API

Using bash:

```bash
./scripts/test-ollama.sh
```

Or with Python:

```bash
python examples/basic_call.py
```

## 🛑 Stop the Server

To stop Ollama when you're done:

```bash
./scripts/stop-ollama.sh
```

---

## 📂 Project Structure

```
ollama-local-ai/
├── scripts/         # install/start/stop/test
├── models/          # model downloads
├── examples/        # Python test + results
├── docs/            # setup + troubleshooting
├── config/          # optional configs
```