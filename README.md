# 🧑‍💻 User Profile Manager (FastAPI)

A simple RESTful API for managing user profiles using **FastAPI** and **JSON file storage**. This project supports full CRUD operations with custom validation and user-friendly error handling.

---

## 📂 Project Structure

├── main.py # FastAPI entrypoint
├── services/
│ └── userService.py # Business logic layer for user operations
├── schemas/
│ └── user.py # Pydantic models (User, UserCreate)
├── utils/
│ └── fileHandler.py # Load/save JSON user data
├── users.json # JSON file used as a database
└── README.md
