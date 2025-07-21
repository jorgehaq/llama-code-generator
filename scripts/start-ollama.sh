# start-ollama.sh
#!/bin/bash
echo "🧠 Starting Ollama server..."
nohup ollama serve > ollama.log 2>&1 &
echo "✅ Ollama running at http://localhost:11434"