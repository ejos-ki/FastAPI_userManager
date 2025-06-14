# ---------- Imports Section
from fastapi import HTTPException                                                               # HTTPException -> Use to raise an error message as well as status code (404, 202, etc) 
from schemas.user import User, UserCreate                                                       # ImportsImports "User" and "UserCreate" class from "./schemas/user.py"
from utils.fileHandler import load_users, save_users

# ---------- Class Section
class UserService:
    # Get <port>/users/<id>, retrieves specific user
    def get_user_by_id(self, user_id: int):
        users = load_users()                                                                   # calls the helper function to read file and load the user

        # Iterate the loaded users from "users.json" file and "users" 
        for user in users:
            if user.id == user_id:                                                             # Each iteration checks if the current iteration matches the passed "id"
                return {"Action": f"Requested User ID of {user_id} found",                     # returns a success message along with the matched user data from iteration
                        "User": user } 
        
        # If after iteration passed "id" is not found 
        raise HTTPException (
            status_code = 404,                                                                 # Raise the status code to 404 to alert that it is a bad request 
            detail = f"Requested User ID {user_id} not found"                                  # Error message "f" to format the message along with the passed "id"
        )

    # Get <port>/users, retrieves all user
    def get_all_users(self):
        users = load_users()                                                                   # calls the helper function to read file and load the user
        
        # if the loaded users is currently empty
        if not users:
            return {
                "message": "No users available, please create a new user",                     # Returns a message 
                "data": []                                                                     # return an empty list
            }
        return {"Action": "All users retrieved successfully", "Users": users}                  # Returns a success message along the users data

    # Post <port>/users, create user data
    def create_user(self, user: UserCreate):
        users = load_users()                                                                   # calls the helper function to read file and load the user
 
        # Iterates to check for duplicate email
        if any(existing_user.email.lower() == user.email.lower() for existing_user in users):  
            raise HTTPException(                                                                  
                status_code = 400,                                                             # 400 Bad Request
                detail = f"Email '{user.email}' is already in use."                            # Error message for duplicate email
            )
    
        # Auto-generate the next ID
        new_id = max([user.id for user in users], default = 0) + 1                             # iterates the loaded users and retrieves the maximum stored "id" and increment by 1

        # Initializes the ne User data set
        user_with_id = User(
            id         = new_id,
            firstName  = user.firstName.title(),
            middleName = user.middleName.title() if user.middleName else None,               
            lastName   = user.lastName.title(),
            suffix     = user.suffix.title() if user.suffix else None,
            email      = user.email,
            role       = user.role.title()
        )

        users.append(user_with_id)                                                             # Appends the newly created User data to the local file
        save_users(users)                                                                      # Calls the helper function and saves the updated User data
        return {"Action": f"User ID {user_with_id.id} created successfully",                   # Success message with the created "id" 
                "User": user_with_id }                                                         # the new set of user data

    # Post <port>/users/<id>, update/edit specified user data
    def update_user(self, user_id: int, data: dict):
        users = load_users()                                                                   # calls the helper function to read file and load the user

        #Iterates the loaded file and retrieves the current user data and the index 
        for index, user in enumerate(users):
            # If the user is matched the passed "user_id"
            if user.id == user_id:
                # formats the updated data
                updated_data = {
                    "firstName" : data.get("firstName", user.firstName).title(),
                    "middleName": data.get("middleName", user.middleName).title() 
                                    if data.get("middleName") 
                                    else user.middleName,
                    "lastName"  : data.get("lastName", user.lastName).title(),
                    "suffix"    : data.get("suffix", user.suffix).title() 
                                    if data.get("suffix") 
                                    else user.suffix,
                    "email"     : data.get("email", user.email),
                    "role"      : data.get("role", user.role).title()
                }

                # checks whether the new role is either "Admin or User"
                if updated_data["role"] not in ["Admin", "User"]:
                    raise HTTPException(
                        status_code = 400,                                                     # Raise the status code to 400 to alert that it is a bad request 
                        detail = "Role must be either 'Admin' or 'User'"                       # Error message
                    )
                
                users[index] = user.model_copy(update=updated_data)                            # copies the updated data to the current position of the former user data
                save_users(users)                                                              # saves the data

                return {"Action": f"User ID {user_id} updated successfully",                   # Success message along the passed user id
                        "User": users[index]}                                                  # Prints the updated user data
        
        # If the passed "user_id" is not found
        raise HTTPException(
            status_code = 404,                                                                 # Raise the status code to 404 to alert that it is a bad request 
            detail = f"Requested User ID {user_id} to update not found"                        # Error message
        )

    # Delete <port>/users/<id>, delete specified user data
    def delete_user(self, user_id: int):
        users = load_users()                                                                   # calls the helper function to read file and load the user

        # iterated the loaded users
        for user in users:
            # if current iteration's "id" matches the passed "id"
            if user.id == user_id:
                users.remove(user)                                                             # removes it from the list
                save_users(users)                                                              # saves the new user data
                return {"Action": f"User ID {user_id} deleted successfully"}                   # returns a success message along the deleted users' is
        
        # If the passed "user_id" is not found
        raise HTTPException(
            status_code = 404,                                                                 # Raise the status code to 404 to alert that it is a bad request 
            detail = f"Requested User ID {user_id} to delete not found"                        # Error message along with the passed "id"
        )