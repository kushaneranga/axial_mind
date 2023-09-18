from fastapi import APIRouter, Depends, HTTPException
from axial_mind.app.controllers.auth.login_controller import login
from axial_mind.app.controllers.auth.logout_controller import logout
from axial_mind.app.controllers.user_controller import register_user, login_user, User

router = APIRouter()

@router.post("/register", response_model=User)
async def register(user: User):
    return register_user(user)

@router.post("/login")
async def user_login(username: str, password: str):
    return login_user(username, password)

@router.post("/logout")
async def user_logout():
    return logout()
