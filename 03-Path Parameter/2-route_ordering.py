from fastapi import FastAPI

app = FastAPI()

# ==============================================================================
# NOTE ON ROUTE ORDERING:
# Static/Specific routes MUST be defined BEFORE dynamic path parameters.
# 
# FastAPI matches routes sequentially from top to bottom.
# If /shipment/{id} were placed FIRST, a request to /shipment/latest would 
# match {id} instead, try to parse the string "latest" as an integer, 
# and raise a 422 Unprocessable Entity validation error.
# ==============================================================================

# 1. Fixed/Static Route: Must come first to prevent "latest" from being swallowed as an ID
@app.get("/shipment/latest") 
def latest_shipment():
    return {
        "ID": None,
        "Product": "Macbook Air",
        "Status": "Shipped"
    }

# 2. Dynamic Route: Catches any integer ID such as "/shipment/101"
@app.get("/shipment/{id}")
def get_shipment(id: int):
    return {
        "ID": id,
        "Product": "Macbook Air",
        "Status": "Shipped"
    }

# To run this server: uvicorn "03-Path Parameter.2-route_ordering:app" --reload
