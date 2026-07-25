from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from pydantic import BaseModel, Field, computed_field
from enum import Enum
from typing import Any

# The Shipment Data
#==================================================================================================
database = {
    101: {"Product": "Asus Motherboard", "Quantity": 1, "Price": 189.99, "Status": "Shipped", "Total Price": 189.99},
    102: {"Product": "Corsair DDR5 RAM 32GB", "Quantity": 2, "Price": 115.00, "Status": "Processing", "Total Price": 230.00},
    103: {"Product": "Logitech MX Master 3S", "Quantity": 1, "Price": 99.99, "Status": "Delivered", "Total Price": 99.99},
    104: {"Product": "Samsung 4K Monitor", "Quantity": 1, "Price": 349.50, "Status": "In Transit", "Total Price": 349.50},
    105: {"Product": "Nvidia RTX 4080 GPU", "Quantity": 1, "Price": 1199.00, "Status": "Pending", "Total Price": 1199.00},
    106: {"Product": "Keychron Mechanical Keyboard", "Quantity": 3, "Price": 85.00, "Status": "Shipped", "Total Price": 255.00}
}
#==================================================================================================

# Pydantic Schema enforcing automatic type validation
#==================================================================================================

# String enum that restricts shipment status fields to a fixed set of predefined options.
class ShipmentStatus(str, Enum):

    Delivered = "Delivered"
    Out_For_Delivery = "Out For Delivery"
    Shipped = "Shipped"
    Processing = "Processing"
    In_Transit = "In Transit"
    Pending = "Pending"

class BaseShipment(BaseModel):
    Product: str = Field(description="Product Name")
    Quantity: int = Field(default=1, gt=0, le=100, description="Number of Units")
    Price: float = Field(gt=0, description="Unit Price of the Product")
    Status: ShipmentStatus = Field(default=ShipmentStatus.Pending, description="Tracking of the Shipment")

    @computed_field(alias="Total Price")
    @property
    def total_price(self) -> float:
        """Calculates the Total Price automatically."""
        return round(self.Price * self.Quantity, 2)

class UpdateShipment(BaseModel):
    Status: ShipmentStatus
#==================================================================================================    

app = FastAPI()

# Create New Shipment Entry via Post Method
@app.post("/create_shipment", status_code=status.HTTP_201_CREATED)
def create_shipment(id: int, shipment: BaseShipment) -> dict[str, Any]:

    if id in database:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Shipment #{id} already exists.")
    
    database[id] = shipment.model_dump(by_alias=True)
    return {"Details": f"Shipment #{id} created successfully", "Data": database[id]}

# Update the Status in an Existing Shipment 
@app.patch("/update_shipment")
def update_shipment(id: int, shipment: UpdateShipment) -> dict[str, Any]:

    if id not in database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Shipment #{id} does not exist.")
    
    database[id]["Status"] = shipment.Status.value
    return {"Detials": f"Shipment at #{id} Updated Successfully"}

# Read the Database via Shipment ID
@app.get("/read_shipment", response_model=BaseShipment)
def read_shipment(id: int):

    if id not in database:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Shipment #{id} does not exist.")
        
    return database[id]

# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scaler API"
    )

# Command to Run the Server:
# uvicorn "06-Pydantic Model.5-summary_project:app" --reload