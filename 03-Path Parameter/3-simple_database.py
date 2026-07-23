from fastapi import FastAPI

db = {
    1101: {
        "Product": "laptop",
        "Status": "Shipped"
    },
    1102: {
        "Product": "Phone",
        "Status": "Shipped"
    },
    1103: {
        "Product": "laptop",
        "Status": "Delivered"
    },
    1104: {
        "Product": "Smart Watch",
        "Status": "Pending"
    }
}


app = FastAPI()

@app.get("/shipment/{id}")
def get_shipment(id: int):

    if id not in db:
        return {"Error": "Not Found"}
    else:
        return db[id]

# To run this server: uvicorn "03-Path Parameter.3-simple_database:app" --reload

# try these in browser:
# http://127.0.0.1:8000/shipment/1101
# http://127.0.0.1:8000/shipment/1102
# http://127.0.0.1:8000/shipment/1103
# http://127.0.0.1:8000/shipment/1104
