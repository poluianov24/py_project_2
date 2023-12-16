try:
    n_1 = float(input("Enter width: "))
    n_2 = float(input("Enter height: "))
    print("\033[35m")
    print("Area of a rectangle: ", n_1 * n_2 / 2)
except Exception as e:
    print(e)