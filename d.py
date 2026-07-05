import time

print("Please insert your card")
time.sleep(2)  # Reduced sleep for faster testing

password = 1234
balance = 5000

try:
    pin = int(input("Enter your ATM pin: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

if pin == password:
    while True:
        print("""
    1 == Balance
    2 == Withdraw
    3 == Deposit
    4 == Exit """)

        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option number.")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")
            
        elif option == 2:
            withdraw_amount = int(input("Please enter withdrawal amount: "))
            if withdraw_amount > balance:
                print("Insufficient funds!")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account.")
                print(f"Your current balance is {balance}")
                
        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account.")
            print(f"Your updated balance is {balance}")
            
        elif option == 4:
            print("Thank you for using our ATM. Goodbye!")
            break
            
        else:
            print("Invalid option, please try again.")
else:
    print("Wrong password. Please try again.")
