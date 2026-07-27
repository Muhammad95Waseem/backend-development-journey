from database import Database
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from schema import BaseShipment, UpdateShipment

db = Database()
app = FastAPI(title="Shipment Management API")


@app.post("/shipments", status_code=status.HTTP_201_CREATED)
def create_shipment(data: BaseShipment):
    new_id = db.insert_data(data)
    return {"message": f"Shipment #{new_id} created successfully", "id": new_id}


@app.patch("/shipments")
def update_shipment(data: UpdateShipment):
    updated = db.update_data(data)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment #{data.id} does not exist.",
        )
    return {"message": f"Shipment #{data.id} updated successfully"}


@app.get("/shipments/{id}")
def read_shipment(id: int):
    shipment = db.get_data(id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment #{id} does not exist.",
        )
    return shipment


@app.delete("/shipments/{id}")
def delete_shipment(id: int):
    deleted = db.delete_data(id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment #{id} does not exist.",
        )
    return {"message": f"Shipment #{id} deleted successfully"}


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )