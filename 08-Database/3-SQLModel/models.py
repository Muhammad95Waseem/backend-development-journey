from sqlmodel import Field, SQLModel
from enum import Enum

class ShipmentStatus(str, Enum):
    DELIVERED = "Delivered"
    OUT_FOR_DELIVERY = "Out For Delivery"
    SHIPPED = "Shipped"
    PROCESSING = "Processing"
    IN_TRANSIT = "In Transit"
    PENDING = "Pending"

class ShipmentModel(SQLModel, table=True):
    __tablename__ = "store.db"

    Id: int = Field(default=None, primary_key=True)
    Product: str 
    Quantity: int = Field(gt=0, le=100)
    Status: ShipmentStatus = Field(default="Pending")
    Price: float | int = Field(gt=0)
