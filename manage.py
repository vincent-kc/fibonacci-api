import sys
from sqlalchemy_utils import create_database, database_exists

from app import models
from app.database import engine


def create_db():
    print("Creating database ...")

    if not database_exists(engine.url):
        create_database(engine.url)
    models.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    globals()[sys.argv[1]]()
