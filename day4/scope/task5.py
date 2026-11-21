mode = "global"

def outer():
    mode = "enclosing"

    def inner():
        mode = "local"
        print("Inside inner:", mode)  # Local

    inner()
    print("Inside outer:", mode)  # Enclosing

outer()
print("Outside:", mode)  # Global