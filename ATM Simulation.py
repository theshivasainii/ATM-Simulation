balance = 1000
transactions = []

def check_balance():
    print("Your current balance is:", balance)

def deposit():
    global balance
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: {amount}")
            print("Amount deposited successfully")
        else:
            print("Invalid amount")
    except:
        print("Enter a valid number")

def withdraw():
    global balance
    try:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            balance -= amount
            transactions.append(f"Withdrawn: {amount}")
            print("Please collect your cash")
    except:
        print("Enter a valid number")

def bank_statement():
    print("\n--- Bank Statement ---")
    if len(transactions) == 0:
        print("No transactions yet")
    else:
        for t in transactions:
            print(t)
    print("Current Balance:", balance)

def atm():
    pin = 1234
    
    try:
        entered_pin = int(input("Enter your PIN: "))
    except:
        print("Invalid PIN")
        return

    if entered_pin != pin:
        print("Wrong PIN")
        return

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Bank Statement")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input")
            continue

        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            bank_statement()
        elif choice == 5:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")

atm()