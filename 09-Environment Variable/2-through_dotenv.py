from dotenv import load_dotenv
import os

load_dotenv()

Password = os.getenv("POSTGRES_PASSWORD")

print(Password)

# Commands to run the file:
# cd "Environment Variable"
# python 2-through_dotenv.py