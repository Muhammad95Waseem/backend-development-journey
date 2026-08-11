# Shipment Management API

A lightweight FastAPI application for managing shipment records using a local JSON-based storage layer.

---

## Quick Start Guide

Ensure you are inside the `backend-development-journey` directory, then run:

```bash
cd 08-Database/1-Json
uvicorn main:app --reload
```

### `Shipments` Table

| Column | Type |
| :--- | :--- |
| **`id`** | `int` |
| **`product`** | `str` |
| **`quantity`** | `int` |
| **`status`** | `str` |
| **`price`** | `float` |


## System Architecture & Data Flow

```
  +-----------------+
  |   HTTP Client   |  (Browser / Scalar / cURL / Postman)
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
                                | shipments.json|  (JSON Data File)
                                +---------------+
```