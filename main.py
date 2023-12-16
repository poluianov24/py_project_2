try:
    n_1 = float(input("Enter a number 1: "))
    n_2 = float(input("Enter a number 2: "))
    n_3 = float(input("Enter a number 3: "))
    print("\033[35m")
    print("Sum: ", n_1 + n_2 + n_3)
    print("Multiplication: ", n_1 * n_2 * n_3)
except Exception as e:
    print(e)