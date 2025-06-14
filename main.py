# ---------- Imports Section
from fastapi import FastAPI, Depends, Body                                              # FastAPI -> Core class used to create the application instance
                                                                                        # Depends -> Used to inject dependencies 
                                                                                        #    Body -> Explicitly declare and extract the request body content
from services.userService import UserService                                            # imports the "UserService" class from "./services/userService.py"
from utils.fileHandler import validate_id                                               # imports the "validate_id" helper function from "./utils/fileHandler"
from schemas.user import UserCreate                                                     # imports the "UserCreate" class from "./schemas/user.py"

# ---------- Variable declaration adn Initialization Section
app = FastAPI()                                                                         # Creates an instance of the FastAPI app
user_service = UserService()                                                            # Create instance of UserService class to handle user-related service

# ---------- Route Section
# Retrieves the specified user through id
@app.get("/users/{id}")                                                                 
def get_user(id: int = Depends(validate_id)):                                           # Sets id as an integer after running it through the validate_id function
    return user_service.get_user_by_id(id)                                              # Calls service method to fetch a user by ID

# Retrieves all the users present
@app.get("/users")                                                                      
def get_users():
    return user_service.get_all_users()                                                 # Calls service method to return all users

# Create new user data
@app.post("/users") 
def create_user(user: UserCreate):                                                      # Define user parameter as the UserCreate schema
    return user_service.create_user(user)                                               # Calls service method to create a new user

# Update existing user data through specified id
@app.put("/users/{id}")
def update_user(id: int = Depends(validate_id), updated_data: dict = Body(...)):        # Validates id from path and gets the new data from the request body
    return user_service.update_user(id, updated_data)                                   # Calls service method to update the user with new data

# Delete existing user data through specified id
@app.delete("/users/{id}")
def delete_user(id: int = Depends(validate_id)):                                        # Validates id from path before deletion
    return user_service.delete_user(id)                                                 # Calls service method to delete the specified user