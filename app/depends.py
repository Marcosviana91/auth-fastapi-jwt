from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.db.connection import Session
from app.auth_user import UserUseCases

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')


def token_verifier(token=Depends(oauth_scheme)):
    uc = UserUseCases()
    uc.verify_token(access_token=token)
