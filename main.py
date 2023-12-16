try:
    n_1 = float(input("Enter a number 1: "))
    n_2 = float(input("Enter a number 2: "))
    print("\033[35m")
    print("Sum: ", n_1 + n_2)
    print("Subtraction: ", n_1 - n_2)
    print("Multiplication: ", n_1 * n_2)
except Exception as e:
    print(e)