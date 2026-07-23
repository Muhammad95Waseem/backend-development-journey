# ==================================================
# 1. Basic Decorator (Manual Function Wrapping)
# ==================================================
def decorator_1(func):

    def wrapper_1():
        print("++++++++++")
        func()
        print("++++++++++")

    return wrapper_1

def display_1():
    print("Hello Guys")

# Manually wrapping the function
d = decorator_1(display_1)
d()


# ==================================================
# 2. Standard Decorator (Using @ Syntax)
# ==================================================
def decorator_2(func):

    def wrapper_2():
        print("++++++++++")
        func()
        print("++++++++++")

    return wrapper_2

@decorator_2
def display_2():
    print("Hello Guys")

display_2()


# ==================================================
# 3. Decorator with Arguments (Configurable Fence Symbol)
# ==================================================
def custom_decorator(symbol: str = "+"):

    def decorator_3(func):

        def wrapper_3(text: str):

            print(symbol * 10)
            func(text)
            print(symbol * 10)

        return wrapper_3
    
    return decorator_3

@custom_decorator("-")
def display_3(text: str):
    print(text)

display_3("Hi Guys")