from fastapi import FastAPI
from langserve import add_routes
from app.rag_chroma.chain import chain
from fastapi.middleware.cors import CORSMiddleware
from app.rag_chroma.schema import Question

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

add_routes(app, 
           chain,
           input_type=Question,
           enable_feedback_endpoint=True,
           enable_public_trace_link_endpoint=True,
           path="/rag")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug", debug=True)
