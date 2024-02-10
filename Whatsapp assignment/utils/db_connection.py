from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker

from utils.config import Config

#########################################
####### Start the RDB Connection ########
#########################################
SQLALCHEMY_DATABASE_URL = Config.read('app', 'db.url')

# check_same_thread argument is needed only for SQLite. It's not needed for other databases.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True,)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session: Session = session()
def get_db_session():

    try:
        yield db_session
    finally:
        db_session.close()
