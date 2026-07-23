from fastapi import FastAPI, status, HTTPException

db = {
    1101: {"Product": "laptop", "Status": "Shipped"},
    1102: {"Product": "Phone", "Status": "Shipped"},
    1103: {"Product": "laptop", "Status": "Delivered"},
    1104: {"Product": "Smart Watch", "Status": "Pending"}
}

app = FastAPI()

# ==============================================================================
#  INCORRECT / FLAGGED PATTERN
# This endpoint works logically, BUT it returns an HTTP 200 OK status code 
# even when the ID is invalid. Client apps (frontend, mobile, external APIs) 
# will see "200 OK" and assume the request succeeded, breaking error handling.
# ==============================================================================
@app.get("/shipment")
def get_product(id: int):
    if id not in db.keys():
        return {"Not Found": "Given ID Does not exist"} # Still sends 200 OK!
    else:
        return db[id]

# ==============================================================================
#  CORRECT / RESTFUL PATTERN
# Using HTTPException halts execution and sends a proper HTTP 404 NOT FOUND status.
# Browsers, Swagger UI, and API clients will correctly register this as a client error.
# ==============================================================================
@app.get("/product")
def get_product(id: int):
    if id not in db.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given ID Does not exist"
        )
    else:
        return db[id]

# To run this server: uvicorn "04-Query Parameter.2-http_exception:app" --reload
