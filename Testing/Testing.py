# Testing class
def ob(ob_func):
    def wrapper(*args):
        obj = ob_func(*args)
        print(f"Testing {type(obj)} object")
        print(obj)
        print("End of Testing")
        return obj
    return wrapper
