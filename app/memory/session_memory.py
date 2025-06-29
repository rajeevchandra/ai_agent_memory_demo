from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

# Initialize memory store
memory = ConversationBufferMemory()

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

def get_memory_response(query):
    return conversation.run(query)