import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from todo_android.models.base import Base


class BaseStorage:
    def __init__(self):
        db_path = os.environ['FLET_APP_STORAGE_DATA']
        db = os.path.join(db_path, 'database.db')
        os.makedirs(os.path.dirname(db), exist_ok=True)
        engine = create_engine(f'sqlite+pysqlite:///{db}', echo=True)
        Base.metadata.create_all(engine)
        self.session = scoped_session(sessionmaker(bind=engine))

    def get_session(self):
        return self.session()
