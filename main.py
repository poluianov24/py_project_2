try:
    n_1 = float(input("Enter a length 1: "))
    n_2 = float(input("Enter a length 2: "))
    print("\033[35m")
    print("area of rhombus: ", n_1 * n_2 / 2)
except Exception as e:
    print(e)