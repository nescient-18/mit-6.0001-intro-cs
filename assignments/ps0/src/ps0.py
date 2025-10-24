from numpy import log2

def get_float(var, must_be_positive=False):
    while True:
        try:
            val = float(input(f"Enter number {var}: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if must_be_positive and val <= 0:  # a direct suggstion from GPT -- see chat log
            print("Must be a positive real number")
            continue
        return val  # a direct suggestion from GPT -- see chat log

if __name__ == "__main__":
    x = get_float(var="x", must_be_positive=True)  # must be positive for valid log domain
    y = get_float(var="y")

    print(f"X**y = {x**y}")  # example output has integer, but I don't think that's a necessary detail
    print(f"log(x) = {log2(x)}")