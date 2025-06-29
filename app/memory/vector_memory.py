from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import VectorStoreRetrieverMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

# Embeddings + FAISS setup
embedding_model = OpenAIEmbeddings()
faiss_store = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

retriever_memory = VectorStoreRetrieverMemory(retriever=faiss_store.as_retriever())

llm = ChatOpenAI(temperature=0)

conversation = ConversationChain(
    llm=llm,
    memory=retriever_memory,
    verbose=True
)

def get_vector_response(query):
    return conversation.run(query)