#!/bin/bash

echo "Starting Ollama server..."
ollama serve &
ollama run llama3
ollama create fsttchatbot -f /model/Modelfile
rm /model/unsloth-llama-3-q4_k_m-unsloth.Q4_K_M.gguf

echo "Waiting for Ollama server to be active..."
while [ "$(ollama list | grep 'NAME')" == "" ]; do
  sleep 1
done