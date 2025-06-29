# AI Agent with Memory (LangChain + Streamlit)

# 🧠 AI Agent with Memory

[![Streamlit App](https://img.shields.io/badge/streamlit-app-brightgreen)](http://localhost:8501)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A production-ready AI agent demo with persistent memory, FAISS vector search, OpenAI/Ollama backend, and LangSmith observability.

## 🚀 Project Summary

This app demonstrates how to build a **context-aware, multi-turn AI agent** using LangChain, with real memory—just like a true assistant.
- 🔁 Switch between buffer and vector memory
- 🤖 Choose OpenAI or Ollama models (local/private)
- 📊 Track interactions with LangSmith observability
- 🐳 Docker & Streamlit for easy deployment

Great for demos, learning, and hackathons!


## Features

- Conversational memory with LangChain
- Streamlit-based interface
- Easily extendable with vector memory

## Setup

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

## Coming soon

- VectorStoreMemory using FAISS
- Event logging using LangSmith
- Knowledge graph integration---

## 🐳 Run with Docker

You can containerize and run the app easily with Docker:

```bash
# Build the Docker image
docker build -t ai-agent-memory .

# Run the container (replace with your OpenAI or Ollama setup)
docker run -e OPENAI_API_KEY=your-api-key -p 8501:8501 ai-agent-memory
```

---

## 🤖 Run with Ollama (instead of OpenAI)

To use a local model via [Ollama](https://ollama.com/):

1. Install Ollama:
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

2. Pull a model (e.g., Mistral):
    ```bash
    ollama pull mistral
    ```

3. Modify `session_memory.py` to use `ChatOllama`:

```python
from langchain_community.chat_models import ChatOllama
llm = ChatOllama(model="mistral")
```

4. Rebuild the Docker image or run locally:
    ```bash
    pip install langchain-community
    ```

------

## 🧠 Advanced Features

### ✅ FAISS Vector Memory

Store long-term conversational history and retrieve context by semantic similarity.

To use it:
```python
from memory.vector_memory import get_vector_response
response = get_vector_response("your query here")
```

Make sure to initialize the FAISS index with your previous chat history.

---

### 📊 LangSmith Observability

Track agent inputs, outputs, and memory traces with LangSmith:

1. Set your environment:
```bash
export LANGCHAIN_API_KEY=your-langsmith-key
export LANGCHAIN_PROJECT=memory-agent-demo
```

2. Use the `@traceable` decorator or import LangSmith in chains.

3. Go to [smith.langchain.com](https://smith.langchain.com) to view trace logs.