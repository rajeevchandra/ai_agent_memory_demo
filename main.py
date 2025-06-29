import streamlit as st

st.set_page_config(page_title="🧠 AI Agent with Memory", layout="centered")
st.title("🧠 Memory-Aware AI Agent")
st.caption("Choose your memory type and model backend to start chatting with context.")

# Sidebar settings
st.sidebar.header("⚙️ Settings")
memory_mode = st.sidebar.radio("Select memory backend", ("Conversation Buffer", "FAISS Vector Memory"))
llm_backend = st.sidebar.radio("Select LLM Backend", ("OpenAI", "Ollama"))
use_langsmith = st.sidebar.checkbox("Enable LangSmith Observability")

if use_langsmith:
    from utils.langsmith_setup import traceable

query = st.text_input("Enter your question:")

if query:
    # Initialize LLM based on user selection
    if llm_backend == "OpenAI":
        from langchain.chat_models import ChatOpenAI
        llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    else:
        from langchain_community.chat_models import ChatOllama
        llm = ChatOllama(model="mistral")

    if memory_mode == "Conversation Buffer":
        from langchain.memory import ConversationBufferMemory
        from langchain.chains import ConversationChain
        # memory = ConversationBufferMemory()
        # chain = ConversationChain(llm=llm, memory=memory, verbose=True)
        if 'memory' not in st.session_state:
            st.session_state.memory = ConversationBufferMemory()

        memory = st.session_state.memory
        chain = ConversationChain(llm=llm, memory=memory, verbose=True)
    elif memory_mode == "FAISS Vector Memory":
        from langchain.vectorstores import FAISS
        from langchain.embeddings import OpenAIEmbeddings
        from langchain.memory import VectorStoreRetrieverMemory
        from langchain.chains import ConversationChain
        embeddings = OpenAIEmbeddings()
        store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        memory = VectorStoreRetrieverMemory(retriever=store.as_retriever())
        chain = ConversationChain(llm=llm, memory=memory, verbose=True)

    if use_langsmith:
        @traceable
        def run_chain():
            return chain.run(query)
        response = run_chain()
    else:
        response = chain.run(query)

    st.markdown("### 🤖 Response:")
    st.write(response)
