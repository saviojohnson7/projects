import time
import pyttsx3

i=pyttsx3.init()

print("WELCOME TO CANARA BANK")
tell = ("WELCOME TO CANARA BANK")
i.say(tell)
i.runAndWait()
print()
print("Please enter your CARD")
v1 = ("Please enter your card")
i.say(v1)
i.runAndWait()
v2 = ("processing")
i.say(v2)
i.runAndWait()

time.sleep(2)
password=1010
balance=10000
chances=3

# while True:
pin = int(input("Enter your PIN: "))

while True:
    if pin!=password:
        print("You have entered the wrong PIN.")
        chances -= 1
        # print()
        print(f"You have {chances} chances left")
        print()
        if chances == 0:
            print("Try again after 30 minutes")
            break
            print("================================")
        pin = int(input("Enter your PIN: "))


    if pin==password:
    #     tell = ("WELCOME TO CANARA BANK")
    #     i.say(tell)
    #     i.runAndWait()


        print("""
        OPTIONS: 
        
        1==Balance
        2==Deposit 
        3==Withdraw Cash
        4==Change PIN
        5==Exit
        """)

        option=int(input("Please enter your choice: "))
        if option==1:
            print("Your balance amount is",balance)

        elif option==2:
            s=int(input("Enter the amount: "))
            x=s+balance
            balance=x
            print("You have successfully deposited Rs",s)
            print("Your total balance is Rs",x)

        elif option==3:
            print("Account type:\n 1-savings 2-current")
            type=input("Enter your account type: ")
            p=int(input("Enter the withdrawal amount: "))
            print("Do you want to print receipt? (Yes or No)")
            receipt=input("Enter: ")


            if receipt=="Yes" or receipt=="yes":
                print("Receipt Generated.")
                time.sleep(2)
            else:
                print("Processed")

            print("You have successfully withdrawed Rs",p)

            if p>balance:
                print("Insufficient balance")
            else:
                w=balance-p
                balance = w
                print()
                print("*** Your total balance is Rs", w,"***")


        elif option==4:
            registered_no = int(input("Enter your registered mobile number: "))
            print()
            print("OTP successfully sent")

            otp=input("Enter the OTP: ")
            time.sleep(2)
            new_pin=int(input("Enter the new PIN: "))
            print("*** PIN successfully changed. ***")



        if option==5:
            print("Thank you for using CANARA BANK ATM !!! \n Visit Again.")
            break
