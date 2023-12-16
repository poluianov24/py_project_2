try:
    n_1 = float(input("Enter the number: "))
    n_2 = float(input("Enter percentage: "))
    print("\033[35m")
    print("Percentage of the number: ", n_1 * n_2 / 100)
except Exception as e:
    print(e)