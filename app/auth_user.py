from datetime import datetime, timedelta
from fastapi import status
from fastapi.exceptions import HTTPException
from app.db.connection import Session
from passlib.context import CryptContext
from jose import jwt, JWTError
from decouple import config
from app.schemas import User

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

crypt_context = CryptContext(schemes=['sha256_crypt'])

class UserUseCases:
    def __init__(self):
        self.db_session = Session


    def user_register(self, user: User):
        new_user: User = {
            "username": user.username,
            "password": crypt_context.hash(user.password)
        }
        try:
            return self.db_session.create_User(new_user)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
            )

    def user_login(self, user: User, expires_in: int = 90):
        user_on_db = self.db_session.get_User(user['username'])

        if not user_on_db:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid username or password'
            )
        
        
        
        if not crypt_context.verify(user['password'], user_on_db['password']):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid username or password'
            )
        
        exp = datetime.utcnow() + timedelta(minutes=expires_in)

        payload = {
            'sub': user['username'],
            'exp': exp
        }

        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return {
            'access_token': access_token,
            'exp': exp.isoformat()
        }

    def verify_token(self, access_token):
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token'
            )
        
        user_on_db = self.db_session.get_User(data['sub'])

        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token'
            )

