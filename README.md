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

#### ✅Requirements
```bash
pip install fastapi uvicorn
```
#### ▶️ Run the API Server
```bash
uvicorn main:app --reload
```




### 🔐 Custom Validation Highlight
Instead of relying solely on FastAPI’s built-in type validation, this project uses a custom validate_id function for cleaner and more readable error messages.

Example:
- FastAPI: 422 Unprocessable Entity
- Custom: 400 Bad Request — Invalid ID 'abc': Not a number

This improves API clarity and user-friendliness.

### 🛠 API Endpoints
#### 📄 Get All Users
```
GET /users
```
Response
```json
{
  "Action": "All users retrieved successfully",
  "Users": [...]
}
```



### ✅ Features
- JSON-based persistence (no database setup needed)
- Custom, readable validation responses
- Duplicate email checking
- Case formatting for names and roles
- Error handling with clear HTTP statuses
- Ready for extension (JWT, role-based auth, etc.)



### 🔐 👨‍👷 Author
Jeo D. Latorre | Developer



### 🔐 📘 Future Enhancements
- JWT authentication
- SQLite backend with SQLAlchemy
- Pagination & filtering
- OpenAPI schema annotations

### 📬 Questions?
Feel free to open an issue or reach out if you want help improving or extending this project.
