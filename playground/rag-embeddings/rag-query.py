import argparse
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain_community.vectorstores import Chroma
from embeddings_function import get_embedding_function

CHROMA_PATH = "chroma-fstt"

PROMPT_TEMPLATE = """
Répondre seulement en français, si le contexte ne répond pas à la question vouz pouvez spéculer, et mentionner que vous n'êtes pas sûr et demander plus de détails ou d'être plus précis.:

{context}

---

Répondre au question suivant avec le context ci-dessus: {question}
"""
## , veuillez répondre avec "Je ne sais pas"

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    
    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=7)
    
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    # print(context_text)
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    model = Ollama(model="llama3", callbacks=callback_manager)
    print(f"\nResponse:\n")
    response_text = model.invoke(prompt)
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    print(f"\n\nSources: {sources}")
    # print(formatted_response)
    return response_text


if __name__ == "__main__":
    main()