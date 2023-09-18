from fastapi import HTTPException
from .models.user import User

# In-memory database for demo purposes (replace with a real database)
users_db = []

def register_user(user: User):
    users_db.append(user)
    return user

def login_user(username: str, password: str):
    for user in users_db:
        if user.username == username and user.password == password:
            return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

def logout_user():
    # Implement logout logic here (if needed)
    pass
