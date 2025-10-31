# LangGraph-ChatBot


An interactive multi-step chatbot built using **LangGraph** and **LangChain**, powered by **GPT-4o**.  
This project demonstrates how to create **stateful conversational workflows** using a graph-based structure.

---

## 🚀 Features

- Built with **LangGraph** — a graph-driven workflow for LLMs.
- Maintains **conversation state** across steps.
- Demonstrates **conditional routing** (looping based on user input).
- Uses **GPT-4o** via LangChain’s `ChatOpenAI` model.

---

## 🧩 Project Flow
Each node represents a step:
1. **get_user_question:** Takes a new user input.
2. **ai_responder:** Calls the GPT-4o model for a response.
3. **ask_continue:** Asks if the user wants to continue chatting.

---

## ⚙️ Setup

### 1. Clone the repository

git clone https://github.com/selimbenhajbraiek/LangGraph-ChatBot.git

pip install -r requirements.txt

please make sure the .env file in the same folder if the python file and contain the OpenAI key: OPENAI_API_KEY = ""

and if you're using the jupyter make sure to add: %load_ext dotenv %dotenv
