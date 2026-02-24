# 🤖 Agentic CSV AI

An end-to-end **Agentic AI system** that allows users to upload CSV or Excel datasets and ask natural language questions for automated data analysis.

Built using **FastAPI**, **LangGraph (ReAct agent)**, **Hugging Face LLM**, and **Pandas**, with a simple frontend UI.

---

## 🚀 Demo Overview

This project enables users to:

- 📂 Upload CSV or Excel datasets
- 💬 Ask natural language questions
- 🧠 Automatically decide which analysis tool to use
- 📊 Generate dataset insights
- 🔍 Detect missing values
- 📈 Compute summary statistics
- 👀 Preview datasets
- 🌐 Use a browser-based frontend interface

---

## 🏗️ System Architecture

User
↓
Frontend (HTML + JS)
↓
FastAPI Backend
↓
LangGraph ReAct Agent
↓
Pandas Tools
↓
LLM Explanation
↓
Response to UI


### 🧠 Agentic Flow

1. User uploads dataset
2. User asks a question
3. ReAct agent reasons step-by-step
4. Agent selects the appropriate tool
5. Pandas processes the dataset
6. LLM explains the result
7. Response is displayed on the frontend

---

## 🛠 Tech Stack

### Backend
- FastAPI
- LangGraph (ReAct agent framework)
- Hugging Face Transformers
- Pandas
- Python 3.11

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### AI Model
- TinyLlama (via Hugging Face)

---

## 📂 Project Structure
agentic_csv_ai/
│
├── app.py # FastAPI backend server
├── agent.py # ReAct agent logic
├── tools.py # Data analysis tools (Pandas)
├── requirements.txt # Python dependencies
│
├── frontend/
│ └── index.html # Frontend UI
│
├── data/ # Uploaded datasets
│
└── README.md



