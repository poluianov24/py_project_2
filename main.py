try:
    n_1 = float(input("Enter salary amount: "))
    n_2 = float(input("Enter the payment amount to the bank: "))
    n_3 = float(input("Enter utility payment: "))
    print("\033[35m")
    print("Spare cash: ", n_1 - n_2 - n_3)
except Exception as e:
    print(e)