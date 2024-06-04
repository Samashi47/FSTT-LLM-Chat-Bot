FROM python:3.11-slim

WORKDIR /code

COPY ./app ./app

RUN pip install langchain fastapi langserve uvicorn langchain_community chromadb ollama
RUN pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install transformers tqdm numpy scikit-learn scipy nltk sentencepiece
RUN pip3 install --no-deps sentence-transformers huggingface-cli sse_starlette
RUN pip install -U "huggingface_hub[cli]"
RUN huggingface-cli download OrdalieTech/Solon-embeddings-large-0.1

CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8000