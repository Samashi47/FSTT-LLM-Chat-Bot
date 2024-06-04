FROM ollama/ollama:latest

WORKDIR /model

COPY ./run_ollama.sh /model/run_ollama.sh
COPY ./unsloth-llama-3-q4_k_m-unsloth.Q4_K_M.gguf /model/
COPY playground/model/Modelfile /model/

RUN chmod +x run_ollama.sh
RUN /model/run_ollama.sh