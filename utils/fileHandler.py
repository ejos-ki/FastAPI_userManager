# ---------- Imports Section
import json, os                                                             #          json -> Encode / decode Python objects to and from JSON strings
                                                                            #            os -> File-system paths, environment variables, and process utilities
from fastapi import HTTPException, Path                                     # HTTPException -> Use to raise an error message as well as status code (404, 202, etc)
                                                                            #          Path -> Declare and validate path parameters in route functions
from schemas.user import User                                               #          User -> Imports "User" class from "./schemas/user.py"

# ---------- Imports Section
USERS_FILE = "users.json"                                                   # Defines the local storage filename 

# ---------- Helper Function Section
def load_users():
    # If "user.json" is missing
    if not os.path.exists(USERS_FILE):                                      #    os.path.exist(<File Name>) -> Checks if the file exists in the directory
        with open(USERS_FILE, "w") as file:                                 #     open(<File Name>, <mode>) -> Opens the file in "w" write mode
            json.dump([], file)                                             # json.dump(<>, <>, <++options) -> Write an empty list to JSON file
    
    with open(USERS_FILE, "r") as file:                                     # open(<File Name>, <mode>) -> Opens the file in "r" read mode
        return [User(**user) for user in json.load(file)]                   # Save the read data from file to "User" class and returns to the caller

def save_users(users):
    with open(USERS_FILE, "w") as file:                                     # open(<File Name>, <mode>) -> Opens the file in "w" write mode
        json.dump([                                                         # json.dump(<object>, <file>, <++options) 
            user.dict() for user in users   ],                              # Converts each User object to a dictionary
            file,                                                           # Target JSON file to save data into
            indent = 2                                                      # Makes JSON output human-readable with indentation
        )

# Takes one parameter
#   [1] id -> Path parameter from the route
#         ::       str -> set the "id" passed as a String 
#         :: Path(...) -> Indicator that the passed "id" is extracted from URL 
#         ::    -> int -> Integer return type hint for function
def validate_id(id: str = Path(...)) -> int:                           
    # If the "id" passed is invalid (not a number)                             
    if not id.isdigit():
        raise HTTPException (                                               
            status_code = 400,                                              # Raise the status code to 400 to alert that it is a bad request                                         
            detail = f"Invalid ID '{id}': Not a number"                     # Error message "f" to format the message along with the passed "id"
        )
    # If the "id" passed is valid number
    return int(id)                                                          # Converts the passed "id" to int data type and return to the caller 
