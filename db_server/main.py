# from sqlalchemy.orm import declarative_base
from tinydb import  TinyDB, Query
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    
class users_DB:
    __user_Search = Query()
    def __init__(self) -> None:
        self.__db = TinyDB('./db_server/user_auth_db.json')
    
    def create_User(self, new_user:User) -> int:
        '''Create a new user and return ID'''
        if not (self.get_User(new_user['username'])):
            return self.__db.insert(new_user)
        else:
            raise ValueError(f'"{new_user["username"]}" is not available')

    def get_User(self, user_name: str)-> bool:
        '''Search for a user_name and returns true if exist.'''
        return bool(self.__db.search(self.__user_Search.username == user_name))
    
    # def verify_User_Pass(user: User):
    #     pass

# Base = declarative_base()
if __name__ == '__main__':
    print('rodando...')
    new_User = {}
    new_User['username'] = 'maria'
    new_User['password'] = '123456'
    
    db = users_DB()
    a= db.create_User(new_User)
    # a = db.get_User('marcos')
    print (a)
