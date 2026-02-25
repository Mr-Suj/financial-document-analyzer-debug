# Financial Document Analyzer — CrewAI Debug Assignment

## 📌 Debugging-Focused GenAI System Stabilization Project

This project demonstrates real-world debugging, dependency resolution, and AI system stabilization using CrewAI and FastAPI.

The objective was not to build a new system, but to analyze, debug, fix, and stabilize an intentionally broken multi-agent financial document analyzer.

---

## 🧠 Project Overview

The system:

- Accepts financial PDF documents via API
- Uses CrewAI agents for financial analysis
- Executes tasks sequentially
- Returns structured analysis output

Architecture Flow:

User Upload → FastAPI → CrewAI Agents → Tool Execution → Analysis Response

---

## 🐛 Major Issues Identified & Fixed

### 1️⃣ CrewAI Import & API Changes
- Outdated Agent import paths
- Updated to latest CrewAI structure
- Fixed LLM initialization errors

### 2️⃣ Dependency Conflicts
- Pydantic v1 incompatible with CrewAI
- Migrated to Pydantic v2-compatible tool structure
- Resolved OpenAI / LiteLLM version conflicts
- Stabilized requirements.txt

### 3️⃣ Tool Architecture Errors
Original issues:
- Tools passed as function references
- Invalid BaseTool schema
- Pydantic validation failures

Fix:
- Implemented proper BaseTool subclass
- Added required typed attributes (`name: str`, `description: str`)
- Passed instantiated tool objects correctly

### 4️⃣ FastAPI Runtime Failures
- Missing `python-multipart`
- Incorrect reload configuration
- 500 Internal Server errors

Resolved via:
```
pip install python-multipart
```

### 5️⃣ Agent Initialization Bugs
- Undefined LLM object
- Incorrect tool injection
- Improper Crew kickoff inputs

Resolved by:
- Proper CrewAI `LLM()` initialization
- Correct `tools=[FinancialDocumentTool()]`
- Correct `kickoff(inputs={"query": query})`

### 6️⃣ OpenAI RateLimit / Quota Error
Encountered:
```
OpenAI RateLimitError: You exceeded your current quota
```

Engineering Decision:
- Implemented mock response fallback
- Preserved full system pipeline validation
- Ensured API endpoint stability without external dependency

This keeps debugging focused on architecture rather than external API limits.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```
git clone https://github.com/Mr-Suj/financial-document-analyzer-debug.git
cd financial-document-analyzer-debug
```

### 2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Run Server
```
python main.py
```

Server runs at:
```
http://127.0.0.1:8000
```

---

## 🌐 API Usage

Open Swagger UI:
```
http://127.0.0.1:8000/docs
```

### POST `/analyze`

Inputs:
- `file` → Upload financial PDF
- `query` → Optional analysis query

Returns:
```
{
  "status": "success",
  "query": "...",
  "analysis": "...",
  "file_processed": "filename.pdf"
}
```

---

## 🧪 Testing

Upload any PDF via Swagger UI.

Expected behavior:
- File saved temporarily
- CrewAI pipeline executes
- JSON response returned
- File cleaned after processing

---

## 🛠 Tech Stack

- Python
- FastAPI
- CrewAI
- Pydantic v2
- Uvicorn
- LiteLLM / OpenAI (optional integration)
- Virtual Environment Isolation

---

## ⭐ Engineering Highlights

- Resolved multi-layer dependency conflicts
- Migrated tools to Pydantic v2 schema
- Stabilized AI agent orchestration
- Implemented mock fallback for API resilience
- Clean API architecture with proper error handling

This project demonstrates strong debugging capability in modern GenAI systems.

---

## 👨‍💻 Author

Sujal Gowda  J M
AI & ML Engineer