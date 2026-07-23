from fastapi import FastAPI

db = {
    1101: {"Product": "laptop", "Status": "Shipped"},
    1102: {"Product": "Phone", "Status": "Shipped"},
    1103: {"Product": "laptop", "Status": "Delivered"},
    1104: {"Product": "Smart Watch", "Status": "Pending"}
}

app = FastAPI()

# Query parameter with id required
@app.get("/shipment")
def get_shipment(id: int):
    return db[id]

# Query parameter with id optional (if id not passed, it will return latest shipment)
@app.get("/product")
def get_product(id: int | None = None):
    if not id:
        id = max(db.keys())
        return db[id]
    else:
        return db[id]


# To run this server: uvicorn "04-Query Parameter.1-basic_query:app" --reload

# Try these in browser:
# http://127.0.0.1:8000/shipment?id=1101
# http://127.0.0.1:8000/shipment

# http://127.0.0.1:8000/product?id=1101
# http://127.0.0.1:8000/product