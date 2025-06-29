import os
from langsmith import traceable

# Set environment variables (can also be set externally)
os.environ["LANGCHAIN_API_KEY"] = "your_langchain_api_key"
os.environ["LANGCHAIN_PROJECT"] = "memory-agent-demo"

# Use @traceable decorator on your LangChain calls