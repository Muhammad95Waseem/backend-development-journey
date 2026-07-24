from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

db = {
    1101: {"Product": "laptop", "Status": "Shipped"},
    1102: {"Product": "Phone", "Status": "Shipped"},
    1103: {"Product": "laptop", "Status": "Delivered"},
    1104: {"Product": "Smart Watch", "Status": "Pending"}
}

app = FastAPI()

# DELETE via Query Parameter
@app.delete("/shipment/delete")
def delete_shipment(id: int):
    db.pop(id)
    return {"details": f"Shipment form {id} is deleted"}

# Retrieve a single shipment by its integer ID via query parameter
@app.get("/get_shipment")
def get_shipment(id: int):
    if id not in db.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="404 Shipment Not found"
            )
    return db[id]

# Scalar API Documentation
@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scaler API"
    )

# To run this Server: uvicorn "05-CRUD Operations.3-delete_method:app" --reload