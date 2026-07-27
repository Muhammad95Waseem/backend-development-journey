from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from schema import BaseShipment, UpdateShipment
from database import Shipment, Save

app = FastAPI()

# Create New Shipment Entry and stores it in shipments.json
@app.post("/create_shipment")
def create_shipment(id: int, data: BaseShipment):
    if id in Shipment.keys():
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"The Shipment at #{id} already exist")

    Shipment[id] = data.model_dump(by_alias=True)
    Save()
    return {"Details": f"Shipment #{id} created successfully", "Data": Shipment[id]}

# Update the Status in an Existing Shipment
@app.patch("/update_shipment")
def update_shipment(id: int, data: UpdateShipment):

    Shipment[id]["Status"] = data.Status.value
    Save()
    return {"Detials": f"Shipment at #{id} Updated Successfully"}

# Deletes a shipment from the shipments.json
@app.delete("/delete_shipment")
def delete_shipment(id: int):
    if id not in Shipment.keys():
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"Shipment #{id} does not exist."
        )
    Shipment.pop(id, None)
    Save()
    return {"Detials": f"Shipment at #{id} Deleted Successfully"}

# Read the Shipments via Shipment ID from the shipments.json
@app.get("/read_shipment", response_model=BaseShipment)
def read_shipment(id: int):

    if id not in Shipment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Shipment #{id} does not exist.")
        
    return Shipment[id]

# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scaler API"
    )

# Commands to Run the Server:
# cd 07-Database/1-Json
# uvicorn main:app --reload