import time
print("please insert your card")
time.sleep(5)
password=1234
pin=int(input("enter you atm pin"))
balance = 5000
if pin == password:
    while true:
  print("""
    1== balance
    2==withdraw balance
    3==deposit balance
    4==exit """ )

    try:
        option=int(input ("please enter your choice"))
    except:
        print("please enter valid option")
    if option==1:
        print(f"your current balance is {balance}")
    if option==2:
        withdraw_amount=int(input("please enter withdraw_amount"))
        balance=balance=withdraw_amount
        print(f"{withdraw_amount}is debited from your account")
        print(f"your current balance is {balance}")
    if ooptin==3:
        deposit_amount=int(input("please enter deposit_amount"))
        balance=balance+deposit_amount
        print(f"{deposit_amount}is creadited to your account")
        print(f"your updated balance is{balance}")
    if option==4:
        break
else:
    print("Wrong password please try again")
