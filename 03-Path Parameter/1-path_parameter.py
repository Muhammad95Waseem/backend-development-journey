from fastapi import FastAPI

app = FastAPI()

@app.get("/shipment/{id}")
def get_shipment(id: int):
    return {
        "ID": id,
        "Product": "Macbook Air",
        "Status": "Shipped"
    }

# To run this server: uvicorn "03-Path Parameter.1-path_parameter:app" --reload

# Past this in browser: http://127.0.0.1:8000/shipment/101