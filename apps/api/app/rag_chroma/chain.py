from langchain_core.pydantic_v1 import BaseModel
from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from app.rag_chroma.schema import Question
import warnings
from langchain_community.embeddings import HuggingFaceEmbeddings

warnings.simplefilter(action='ignore', category=FutureWarning)

CHROMA_PATH = "app/rag_chroma/chroma-fstt"

PROMPT_TEMPLATE = """
Répondre seulement en français, si le contexte ne répond pas à la question vouz pouvez spéculer, et mentionner que vous n'êtes pas sûr et demander plus de détails ou d'être plus précis.:

{context}

---

Répondre au question suivant avec le context ci-dessus: {question}
"""

vectorstore = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=HuggingFaceEmbeddings(model_name="OrdalieTech/Solon-embeddings-large-0.1", model_kwargs = {'device': 'cpu'}),
)

retriever = vectorstore.as_retriever(search_kwargs={'k': 7})

prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

# LLM
model = Ollama(model="llama3", base_url="http://ModelsHandler:11434")

# RAG chain
chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | model
    | StrOutputParser()
).with_types(input_type=Question)