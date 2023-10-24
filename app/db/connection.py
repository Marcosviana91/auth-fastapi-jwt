# from decouple import config
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from app.db.base import users_DB

# DB_URL = config('DB_URL')

# engine = create_engine(DB_URL, pool_pre_ping=True)
# Session = sessionmaker(bind=engine)
Session =  users_DB()
