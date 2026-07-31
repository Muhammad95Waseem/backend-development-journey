from pydantic import BaseModel, Field, computed_field
from enum import Enum

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
    Id: int = Field(description="Shipment Unique ID", gt=0)
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
