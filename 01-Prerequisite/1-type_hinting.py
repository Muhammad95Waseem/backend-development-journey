#===========================================
# Hinting a Variable type
#===========================================

# Hinting a String
name: str = "Waseem"

# Hinting an Integer
age: int = 25

# Hinting a Float
price: float = 19.99

# Hinting a Boolean
is_active: bool = True

#===========================================
# Hinting Iterable type
#===========================================

# Hinting a List of strings
users: list[str] = ["Waseem", "Ali", "Sara"]

# Hinting a Dictionary with String keys and Integer values
scores: dict[str, int] = {"Waseem": 95, "Ali": 88}

# Hinting a Set of integers
unique_ids: set[int] = {101, 102, 103}

# Hinting a Tuple with fixed types in order
point: tuple[int, int] = (10, 20)

# Hinting a Tuple of variable length containing floats
coordinates: tuple[float, ...] = (1.5, 2.7, 3.14)

#===========================================
# Hinting multiple types
#===========================================

# Hinting a variable that can be None or a String
middle_name: str | None = None

# Hinting a variable that can be multiple types
user_id: int | str = "USR-9021"


#===========================================
# Hinting Function parameters and Return type
#===========================================

# Hinting a Function that returns string
def greet(user_name: str) -> str:
    return f"Hello, {user_name}!"

# Hinting a Function that returns nothing
def log_message(message: str) -> None:
    print(f"LOG: {message}")


#===========================================
# Hinting with Advanced types
#===========================================

# Hinting Any type (disables type checking for this variable)
from typing import Any
data: Any = "Could be anything"

# Hinting a Constant with specific allowed values (Literal)
from typing import Literal
status: Literal["pending", "approved", "rejected"] = "pending"

# Hinting a Custom Class instance
class Car:
    pass

my_car: Car = Car()