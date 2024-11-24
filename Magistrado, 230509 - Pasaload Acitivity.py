#Magistrado, 230509 - Pasaload Acitivity

import threading

lock = threading.Lock()

balances = {}

def buy_load(mobile_number, amount):
    lock.acquire()
    try:
        if mobile_number not in balances:
            balances[mobile_number] = 0
        balances[mobile_number] += amount
        print(f"{amount} pesos load has been successfully bought for mobile number {mobile_number}.")
    finally:
        lock.release()

def check_balance(mobile_number):
    lock.acquire()
    try:
        balance = balances.get(mobile_number, 0)
        print(f"The current balance for mobile number {mobile_number} is {balance} pesos.")
    finally:
        lock.release()

mobile_number = input("Enter mobile number: ")

while True:
    print("Select an option:")
    print("1. Change mobile number")
    print("2. Buy load")
    print("3. Check balance")
    print("4. Exit")

    option = input("Enter option number: ")

    if option == "1":
        mobile_number = input("Enter new mobile number: ")
    elif option == "2":
        print("Select amount to buy load:")
        print("1. 10 pesos")
        print("2. 20 pesos")
        print("3. 50 pesos")
        print("4. 100 pesos")
        print("5. Custom amount")

        amount_option = input("Enter option number: ")

        if amount_option == "1":
            amount = 10
        elif amount_option == "2":
            amount = 20
        elif amount_option == "3":
            amount = 50
        elif amount_option == "4":
            amount = 100
        elif amount_option == "5":
            amount = input("Enter custom amount: ")
            try:
                amount = int(amount)
            except ValueError:
                print("Invalid amount entered.")
                continue
        else:
            print("Invalid option selected.")
            continue

        t = threading.Thread(target=buy_load, args=(mobile_number, amount))
        t.start()
    elif option == "3":
        t = threading.Thread(target=check_balance, args=(mobile_number,))
        t.start()
    elif option == "4":
        break
    else:
        print("Invalid option selected.")
        continue
