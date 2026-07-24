from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

db = {
    1101: {"Product": "laptop", "Status": "Shipped"},
    1102: {"Product": "Phone", "Status": "Shipped"},
    1103: {"Product": "laptop", "Status": "Delivered"},
    1104: {"Product": "Smart Watch", "Status": "Pending"}
}

app = FastAPI()

# Create a new shipment using QUERY PARAMETERS such as "/shipment?product=laptop&status=Shipped"
# Note: In FastAPI, primitive types (like str) without body declarations default to query parameters.
@app.post("/shipment")
def post_shipment(product: str, status: str):

    new_id = max(db.keys()) + 1

    db[new_id] = {
        "Product": product,
        "Status": status
    }
    return {"Details": f"Entry at {new_id} successful"}

# Create a new shipment using a REQUEST BODY payload
# Passing a dict (or Pydantic model) tells FastAPI to expect JSON in the request body.
@app.post("/post_body")
def post_through_body(data: dict[str, str]):

    new_id = max(db.keys()) + 1
    db[new_id] = data
    return {"Details": f"Entry at {new_id} successful"}

# Retrieve a single shipment by its integer ID via query parameter
@app.get("/get_shipment")
def get_shipment(id: int):
    return db[id]


# NOTE: Browsers send a GET request when accessing URLs directly via the address bar.
# Accessing "/shipment?product=ipad&status=Shipped" in a browser tab will yield
# 405 Method Not Allowed. Use Swagger UI or scalar or cURL to send an HTTP POST.
@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scaler API"
    )

# To run this server: uvicorn "04-Query Parameter.3-post_method:app" --reload
