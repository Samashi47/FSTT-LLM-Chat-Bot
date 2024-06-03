from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from app.rag_chroma.schema import Question
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
import argparse
import warnings
from langchain_community.embeddings import HuggingFaceEmbeddings

warnings.simplefilter(action='ignore', category=FutureWarning)

PROMPT_TEMPLATE = """
Répondre seulement en français, si le contexte ne répond pas à la question vouz pouvez spéculer, et mentionner que vous n'êtes pas sûr et demander plus de détails ou d'être plus précis.:

{context}

---

Répondre au question suivant avec le context ci-dessus: {question}
"""

vectorstore = Chroma.from_texts(
    [""],
    collection_name="chroma-fstt",
    embedding=HuggingFaceEmbeddings(model_name="OrdalieTech/Solon-embeddings-large-0.1", model_kwargs = {'device': 'cpu'}),
)
retriever = vectorstore.as_retriever(search_kwargs={'k': 5})
prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

# LLM
model = Ollama(model="fsttchatbot:latest")

# RAG chain
chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | model
    | StrOutputParser()
)


chain = chain.with_types(input_type=Question)