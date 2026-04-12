from typing_extensions import TypedDict
from typing import Annotated
import operator

from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

import os
from dotenv import load_dotenv

load_dotenv()

# LLM Setup
llm = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="openai"
)

# State


class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]

# Node


def chatbot(state: State):
    print("\nInside ChatBot Node")

    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }


# Graph
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# MongoDB Checkpointer
DB_URI = "mongodb://localhost:27017/langgraph_db"

with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:

    graph_with_checkpoint = graph_builder.compile(checkpointer=checkpointer)

    config = {
        "configurable": {
            "thread_id": "abhay"   # memory session id
        }
    }

    # Run
    for chunk in graph_with_checkpoint.stream(
        {
            "messages": [
            HumanMessage(content="What is my name ?")
            ]
        },
        config=config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()


# START -> chatbot -> END

# State = {messages: ["Hey There"] }
# node runs: ChatBot(state: ["Hey There"]) -> ["Hello! This is a message from ChatBot Node. "]
# state = ["Hey There", "Hello! This is a message from ChatBot Node. "]

# checkpoint is now abhay
