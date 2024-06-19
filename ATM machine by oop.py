class Atm:
    def __init__(self):   #_init_ is a constructor.
        self.pin = ""
        self.balance = 0

        self.menu()
    def menu(self):
        user_input = input("""
        Hello, How would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """)

        if user_input =="1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("exit")

    def create_pin(self):
        self.pin = input("Enter your PIN for PIN setup: ")
        print(" PIN set successfully")

    def deposit(self):
        temp = input("Enter your PIN for deposit money: ")
        if temp == self.pin:
            amount = int(input("Enter the amount that you want to deposit:  "))
            self.balance = self.balance + amount
            print("Deposit Successful")
        else:
            print("Invalid PIN")
    def withdraw(self):
        temp = input("Enter your PIN for withdraw money: ")
        if temp == self.pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Operation Successful")

            else:
                print("Insufficient funds")
        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter your PIN to check balance: ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid PIN")



sbi = Atm()
sbi.deposit()
sbi.check_balance()
sbi.withdraw()
sbi.check_balance()


hdfc = Atm()
hdfc.deposit()
hdfc.check_balance()
hdfc.withdraw()
hdfc.check_balance()

print("Check balance for sbi account: ")
sbi.check_balance()  #Check balance for  sbi object
print("Check balance for hdfc account: ")
hdfc.check_balance() #check balance for hdfc object