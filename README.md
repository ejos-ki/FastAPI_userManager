# 🧑‍💻 User Profile Manager (FastAPI)

A simple RESTful API for managing user profiles using FastAPI and JSON file storage. This service supports CRUD operations and includes custom validation and user-friendly error handling.

📂 Project Structure
├── main.py                  # FastAPI entrypoint
├── services/
│   └── userService.py       # Business logic layer for user operations
├── schemas/
│   └── user.py              # Pydantic models (User, UserCreate)
├── utils/
│   └── fileHandler.py       # Load/save JSON user data
├── users.json               # JSON file used as a database
└── README.md

🚀 How to Run
Requirements
  [1] Python 3.10+
  [2] FastAPI
  [3] Uvicorn

Install Dependencies
pip install fastapi uvicorn

Run the API Server
uvicorn main:app --reload
| API will be available at: http://localhost:8000

🔐 Custom Validation Highlight

Instead of relying solely on FastAPI’s built-in type validation, this project uses a custom validate_id function for cleaner and more readable error messages.

Example:
    [] FastAPI: 422 Unprocessable Entity
    [] Custom: 400 Bad Request — Invalid ID 'abc': Not a number
This improves API clarity and user-friendliness.

🛠 API Endpoints

📄 Get All Users
GET /users

Response
{
  "Action": "All users retrieved successfully",
  "Users": [...]
}

🔍 Get User by ID
Success
{
  "Action": "Requested User ID of 1 found",
  "User": {...}
}
Error
{
  "detail": "Requested User ID 99 not found"
}
