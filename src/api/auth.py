import jwt
from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext

from src.database import async_session_maker
from src.schemas.user import UserRequestAdd, UserAdd, User
from src.repositories.user import UserRepositories


router = APIRouter(prefix="/auth", tags=["Аутентификация и авторизация пользователей"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expired_in = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expired_in})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)


@router.post("/register")
async def create_user(user_data: UserRequestAdd):
    hashed_password = pwd_context.hash(user_data.password)
    new_user_data = UserAdd(email=user_data.email, password=hashed_password)
    async with async_session_maker() as session:
        is_exist = await UserRepositories(session).check_exist(user_data.email)
        if is_exist:
            return {"result": "User are already registered"}
        await UserRepositories(session).add(new_user_data)
        await session.commit()
        return {"result": "OK"}

@router.post("/login")
async def login_user(user_data: UserRequestAdd):
    async with async_session_maker() as session:
        user = await UserRepositories(session).get_one_or_none(
            email=user_data.email,
        )
        if not user:
            return HTTPException(status_code=401, detail="User does not exist")
        return {"access_token":create_access_token({"user:_id": user.id})}