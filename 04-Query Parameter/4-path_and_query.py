from fastapi import FastAPI

db = {
    1101: {"Product": "laptop", "Status": "Shipped"},
    1102: {"Product": "Phone", "Status": "Shipped"},
    1103: {"Product": "laptop", "Status": "Delivered"},
    1104: {"Product": "Smart Watch", "Status": "Pending"}
}

app = FastAPI()

@app.get("/shipment/{field}")       # field is the path parameter
def shipment(field: str, id: int):  # id in the query parameter
    return {
        field: db[id][field]
    } 

# To run this server: uvicorn "04-Query Parameter.4-path_and_query:app" --reload

# Try these in browser: 
# http://127.0.0.1:8000/shipment/Product?id=1101
# http://127.0.0.1:8000/shipment/Status?id=1101
