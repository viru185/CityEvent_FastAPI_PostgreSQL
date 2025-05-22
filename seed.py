from app.db.init_db import init_db
from app.utils.populate import Populate

if __name__ == "__main__":
    init_db()
    Populate.run(n=50)
