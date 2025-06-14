# 🧑‍💻 User Profile Manager (FastAPI)

A simple RESTful API for managing user profiles using **FastAPI** and **JSON file storage**. This project supports full CRUD operations with custom validation and user-friendly error handling.

---

### 📂 Project Structure

```
├── main.py                  # FastAPI entrypoint
├── services/
│   └── userService.py       # Business logic for user operations
├── schemas/
│   └── user.py              # Pydantic models (User, UserCreate)
├── utils/
│   └── fileHandler.py       # JSON file load/save helpers
├── users.json               # Simulated database (JSON file)
└── README.md
```

### 📂 Project Structure
#### ✅Requirements
- Python 3.10+
- FastAPI
- Uvicorn
