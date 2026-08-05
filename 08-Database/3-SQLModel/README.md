# SQLModel FastAPI Application

SQLModel combines SQLAlchemy and Pydantic into a single interface, allowing you to define database models that automatically handle data validation, serialization, and database interactions without separate Pydantic schemas.

---

## System Architecture & Data Flow

```
+-----------------+
|   HTTP Client   |  (Browser / Scalar / cURL)
+-----------------+
         |
         | HTTP Requests
         v
+-----------------+
|     main.py     |  (FastAPI Router, Endpoints, Lifespan Handler, Scalar Docs)
+--------+--------+
         |        \
         |         \
         v          v
+-----------------+  +-----------------+
|    schema.py    |  |   session.py    |
+-----------------+  +-----------------+
| SQLModel        |           |
| Schemas & Table |           v
+-----------------+  +-----------------+
                     |    store.db     |  (SQLite DB File)
                     +-----------------+
```

---

## Running the Server

Run the following commands from your project root:

```bash
cd 07-Database/3-SQLModel
uvicorn main:app --reload
```
