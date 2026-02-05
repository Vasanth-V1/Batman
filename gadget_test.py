# Simple Gadget Code
def add_gadget(a, b):
    return a + b

if __name__ == "__main__":
    result = add_gadget(5, 5)
    print(f"Gadget Test: 5 + 5 = {result}")
    if result == 10:
        print("Gadget is working perfectly!")
    else:
        print("Gadget failed the test.")
