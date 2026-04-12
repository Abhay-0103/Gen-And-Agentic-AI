from typing_extensions import TypedDict
from typing import Annotated
import operator

from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

import os
from dotenv import load_dotenv

load_dotenv()

# LLM Setup (Gemini via OpenAI-compatible API)
llm = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="openai"
)

# State Definition
class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]

# Chatbot Node (LLM)
def chatbot(state: State):
    print("\nInside ChatBot Node")

    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }

# Sample Node
def samplenode(state: State):
    print("\nInside Sample Node")

    return {
        "messages": [
            AIMessage(content="Sample Message Appended")
        ]
    }

# Graph Build
graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

# Run
updated_state = graph.invoke({
    "messages": [HumanMessage(content="Hi, My name is Abhay Singh")]
})

print("\nFinal State:\n", updated_state)

# START -> chatbot -> samplenode -> END

# State = {messages: ["Hey There"] }
# node runs: ChatBot(state: ["Hey There"]) -> ["Hello! This is a message from ChatBot Node. "]
# state = ["Hey There", "Hello! This is a message from ChatBot Node. "]
