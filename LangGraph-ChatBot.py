"""
Author: Selim Ben Haj Braiek
Project: LangGraph-ChatBot
Description: An interactive chatbot using LangGraph and LangChain with OpenAI's GPT-4o model.
  
""" 

# conversational_graph.py

from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, BaseMessage
from collections.abc import Sequence
from typing import Literal

# Define the shared conversation state

class ConversationState(TypedDict):
    history: Sequence[BaseMessage]


# Initialize the OpenAI chat model
assistant = ChatOpenAI(
    model="gpt-4o",
    seed=123,
    temperature=0,
    max_completion_tokens=100
)


# Step 1: Ask the user a question
def get_user_question(state: ConversationState) -> ConversationState:
    print("\n Please enter your question for the AI:")
    question = input("You: ")
    return ConversationState(history=[HumanMessage(question)])


# Step 2: Let the assistant respond
def ai_responder(state: ConversationState) -> ConversationState:
    print("\n AI is generating a response...")
    response = assistant.invoke(state["history"])
    response.pretty_print()
    return ConversationState(history=[response])


# Step 3: Ask if user wants to continue
def ask_continue(state: ConversationState) -> ConversationState:
    print("\n Would you like to ask another question? (yes/no)")
    user_reply = input("You: ")
    return ConversationState(history=[HumanMessage(user_reply.lower())])


# Routing logic (conditional edge)

def next_step_router(state: ConversationState) -> Literal["get_user_question", "__end__"]:
    if state["history"][0].content.strip().lower() == "yes":
        return "get_user_question"
    else:
        return "__end__"


# Build the LangGraph workflow

conversation_graph = StateGraph(ConversationState)

conversation_graph.add_node("get_user_question", get_user_question)
conversation_graph.add_node("ai_responder", ai_responder)
conversation_graph.add_node("ask_continue", ask_continue)

conversation_graph.add_edge(START, "get_user_question")
conversation_graph.add_edge("get_user_question", "ai_responder")
conversation_graph.add_edge("ai_responder", "ask_continue")

conversation_graph.add_conditional_edges(
    source="ask_continue",
    path=next_step_router
)

compiled_graph = conversation_graph.compile()

# Run the conversation loop

if __name__ == "__main__":
    print(" Starting Interactive LangGraph Chat...")
    compiled_graph.invoke(ConversationState(history=[]))
