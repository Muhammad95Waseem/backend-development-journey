from enum import Enum
from pydantic import BaseModel, Field


class ShipmentStatus(str, Enum):
    DELIVERED = "Delivered"
    OUT_FOR_DELIVERY = "Out For Delivery"
    SHIPPED = "Shipped"
    PROCESSING = "Processing"
    IN_TRANSIT = "In Transit"
    PENDING = "Pending"


class BaseShipment(BaseModel):
    product: str = Field(description="Product Name")
    quantity: int = Field(default=1, gt=0, le=100, description="Number of Units")
    status: ShipmentStatus = Field(
        default=ShipmentStatus.PENDING, description="Tracking Status"
    )
    price: float = Field(gt=0, description="Unit Price of the Product")


class UpdateShipment(BaseModel):
    id: int = Field(gt=0, description="Shipment Unique ID")
    status: ShipmentStatus