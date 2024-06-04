import argparse
import os
import shutil
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders.word_document import UnstructuredWordDocumentLoader
from langchain_community.document_loaders.powerpoint import UnstructuredPowerPointLoader
from langchain_community.document_loaders import TextLoader
from embeddings_function import get_embedding_function

CHROMA_PATH = "chroma-fstt"
DATA_PATH = "/kaggle/input/fstt-data-init"

def main():

    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    # Create (or update) the data store.
    documents = load_documents()
    chunks = split_documents(documents)
    add_to_chroma(chunks)


# Define a function to create a DirectoryLoader for a specific file type
def create_directory_loader(file_type, directory_path):
    # Define a dictionary to map file extensions to their respective loaders
    loaders = {
        '.doc': UnstructuredWordDocumentLoader,
        '.docx': UnstructuredWordDocumentLoader,
        '.ppt': UnstructuredPowerPointLoader,
        '.pptx': UnstructuredPowerPointLoader
    }
    return DirectoryLoader(
        path=directory_path,
        glob=f"**/*{file_type}",
        loader_cls=loaders[file_type],
    )

def load_documents():
    txt_loader = TextLoader(DATA_PATH+'/uni_info.txt', encoding='utf-8')
    pdf_document_loader = PyPDFDirectoryLoader(DATA_PATH)
    docx_document_loader = create_directory_loader('.docx', DATA_PATH)
    ppt_loader = create_directory_loader('.ppt', DATA_PATH)
    pptx_loader = create_directory_loader('.pptx', DATA_PATH)
    
    txt_documents = txt_loader.load()
    print(f"Number of TXT documents: {len(txt_documents)}")
    pdf_documents = pdf_document_loader.load()
    print(f"Number of PDF documents: {len(pdf_documents)}")
    docx_documents = docx_document_loader.load()
    print(f"Number of DOCX documents: {len(docx_documents)}")
    ppt_documents = ppt_loader.load()
    print(f"Number of PPT documents: {len(ppt_documents)}")
    pptx_documents = pptx_loader.load()
    print(f"Number of PPTX documents: {len(pptx_documents)}")
    documents = pdf_documents  + ppt_documents + pptx_documents + docx_documents + txt_documents
    return documents


def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=0,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)


def add_to_chroma(chunks: list[Document]):
    # Load the existing database.
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    # Calculate Page IDs.
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        # db.persist()
    else:
        print("✅ No new documents to add")


def calculate_chunk_ids(chunks):

    # This will create IDs like "data/monopoly.pdf:6:2"
    # Page Source : Page Number : Chunk Index

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks


def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)


if __name__ == "__main__":
    main()