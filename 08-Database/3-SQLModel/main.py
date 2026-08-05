from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status, Depends
from scalar_fastapi import get_scalar_api_reference
from sqlmodel import Session
from schema import BaseShipment, UpdateShipment
from session import create_db_table, get_session

# Initialize database schema on startup
@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_table()
    yield

app = FastAPI(lifespan=lifespan_handler)

# Fetch a single shipment by ID
@app.get("/read_shipment")
def read_shipment(id: int, session: Session = Depends(get_session)):
    shipment = session.get(BaseShipment, id)

    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!",
        )
    return shipment

# Create a new shipment entry
@app.post("/shipment", response_model=None)
def submit_shipment(shipment: BaseShipment, session: Session = Depends(get_session)):  # Fixed: removed ()
    new_shipment = BaseShipment(
        **shipment.model_dump()
    )
    session.add(new_shipment)
    session.commit()
    session.refresh(new_shipment)

    return {"Details": f"New Shipment added at #{new_shipment.id}"}

# Partially update existing shipment fields
@app.patch("/update_shipment")
def update_shipment(status: UpdateShipment, session: Session = Depends(get_session)):
    update = status.model_dump(exclude_none=True)

    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data provided to update",
        )
    
    order = session.get(BaseShipment, status.id)
    order.sqlmodel_update(update)
    session.add(order)
    session.commit()
    session.refresh(order)

    return {"Details": f"Shipment Updated at #{status.id} to {status.status.value}"}

# Delete a shipment by ID
@app.delete("/delete_shipment")
def delete_shipment(id: int, session: Session = Depends(get_session)):
    session.delete(session.get(BaseShipment, id))
    session.commit
    return {"Details": f"Shipment from #{id} deleted Successfully!"}

# Render Scalar API documentation UI
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )

# Commands to Run the Server:
# cd 08-Database/3-SQLModel
# uvicorn main:app --reload