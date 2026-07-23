from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

db = {
    1101: {"Product": "laptop", "Status": "Shipped"},
    1102: {"Product": "Phone", "Status": "Shipped"},
    1103: {"Product": "laptop", "Status": "Delivered"},
    1104: {"Product": "Smart Watch", "Status": "Pending"}
}

app = FastAPI()

# Creating a new entry through post method
@app.post("/shipment")
def get_shipment(product: str, status: str):

    new_id = max(db.keys()) + 1

    db[new_id] = {
        "Product": product,
        "Status": status
    }

    return {"Id": new_id}

# view the latest entry we make through post method
@app.get("/shipment/latest")
def latest_shipment():
    return db[max(db.keys())]


# NOTE: Browsers send a GET request when accessing URLs directly via the address bar.
# Accessing http://127.0.0.1:8000/shipment?product=ipad&status=Shipped in a browser tab will yield
# 405 Method Not Allowed. Use Swagger UI or scalar or cURL to send an HTTP POST.
@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scaler API"
    )

# To run this server: uvicorn "04-Query Parameter.3-post_method:app" --reload
