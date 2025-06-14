# ---------- Imports Section                                            
from pydantic import BaseModel, EmailStr, Field             # BaseModel -> Base class for data validation and serialization
                                                            #  EmailStr -> Type value ensures that the string is in a valid email format
                                                            #     Field -> Adds extra validation rules
from typing import Literal                                  #   Literal -> Restricts a field to specific fixed values

# ---------- Class Section
class User(BaseModel):                                      # "User" -> for general use
    id         : int = Field(..., gt=0)                     # Ensures that "id" is positive number "gt" = greater than
    firstName  : str
    middleName : str | None = None                          # Optional field, allows null/None
    lastName   : str 
    suffix     : str | None = None                          # Optional field, allows null/None
    email      : EmailStr                                   # Ensures that the string is in a valid email format
    role       : Literal["Admin", "User"]                   # Defines the acceptable value

class UserCreate(BaseModel):                                # Used in creating / Post method of "user.json"
    firstName  : str
    middleName : str | None = None                          # Optional field, allows null/None
    lastName   : str
    suffix     : str | None = None                          # Optional field, allows null/None
    email      : EmailStr                                   # Ensures that the string is in a valid email format
    role       : Literal["Admin", "User"]                   # Defines the acceptable value