from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

# Configure the SQLite database engine.
# - url: Specifies SQLite as the database driver and store.db as the file path.
# - echo=True: Enables SQL statement logging in the terminal for debugging.
# - check_same_thread=False: Allows SQLite connection sharing across multiple threads, 
#   which is required by FastAPI's asynchronous request handling.
engine = create_engine(
    url="sqlite:///store.db",
    echo=True,
    connect_args={"check_same_thread": False}
)

# Imports models inside the function to avoid circular import issues, 
# then registers all SQLModel table metadata and creates any missing tables in the target SQLite database.
def create_db_table():
    from schema import BaseShipment
    SQLModel.metadata.create_all(bind=engine)

# Context-managed dependency function for FastAPI.
# Spawns a dedicated database session per incoming web request, yields it to 
# the route handler, and ensures the session automatically closes once done.
def get_session():
    with Session(bind=engine) as session:
        yield session  