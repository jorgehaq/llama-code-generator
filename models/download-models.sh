#!/bin/bash
echo "⬇️  Descargando modelos Ollama..."

# Verifica si Ollama está instalado
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama no está instalado. Ejecuta primero: ./scripts/install-ollama.sh"
    exit 1
fi

# Modelos que puedes añadir aquí
MODELS=("llama2")

for model in "${MODELS[@]}"
do
    echo "🔽 Descargando modelo: $model"
    ollama pull "$model"
done

echo "✅ Todos los modelos fueron descargados correctamente."