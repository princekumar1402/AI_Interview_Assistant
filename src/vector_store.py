from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from src.config import EMBEDDING_MODEL, TOP_K

def create_vector_store(chunks):
    """
    Create FAISS vector store from resume chunks.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store


def get_retriever(vector_store):
    """
    Convert FAISS vector store into retriever.
    """

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K}
    )

    return retriever