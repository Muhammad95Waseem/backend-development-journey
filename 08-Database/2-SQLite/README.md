## Quick Start Guide


1. Make sure you are in `backend-development-journey` directory

```bash
cd 08-Database/2-SQLite
uvicorn main:app --reload
```

## Database Schema

The SQLite database (`store.db`) contains a primary table named `Shipments` structured as follows:

### `Shipments` Table

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| **`id`** | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Unique shipment identifier |
| **`product`** | `TEXT` | `NOT NULL` | Name of the product |
| **`quantity`** | `INTEGER` | `NOT NULL` | Number of units (1 – 100) |
| **`status`** | `TEXT` | `NOT NULL` (ENUM) | Current shipment state |
| **`price`** | `REAL` | `NOT NULL` | Unit price of item |

---

## System Architecture & Data Flow

```text
  +-----------------+
  |   HTTP Client   |  (Browser / Scalar / cURL)
  +--------+--------+
           |
           | HTTP Requests
           v
  +-----------------+
  |     main.py     |  (FastAPI Router, Endpoints, HTTP Handlers, Docs Route)
  +---+---------+---+
      |         |
      |         +-----------------------+
      v                                 v
+-----------+                   +---------------+
| schema.py |                   |  database.py  |
+-----------+                   +-------+-------+
| Pydantic  |                           |
| Models    |                           v
+-----------+                   +---------------+
                                |   store.db    |  (SQLite DB File)
                                +---------------+