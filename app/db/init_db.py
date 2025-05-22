from app.db.session import engine
from app.db.base import Base
from app.models import event


def init_db():
    print("Creating table...")
    Base.metadata.create_all(bind=engine)
    print("Table created successfully.")


if __name__ == "__main__":
    init_db()
