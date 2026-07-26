import json

# Reads the File "shipment.json"
with open("shipments.json") as file:
    data = json.load(file)

# Converts the data into key-value pair with ID as keys.
Shipment = {}
for order in data:
    Shipment[order["Id"]] = order

# Saves the updated Shipment data lacated in the memory to the shipments.json
def Save():
    with open("shipments.json", "w") as file:
        json.dump(list(Shipment.values()), file)
