class BankSystem():
  
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        deposit_amount = float(input("How much would you like to deposit?"))
        # Add the deposit_amount to the account balance
        self.balance += deposit_amount
        print("Deposit successful")

bank = BankSystem(100)  # Example: initial balance is 100
user_input = input("Do you want to deposit? (yes/no)")
if user_input.lower() == "yes":
    bank.deposit()
else:
    print("No deposit will be made.")
  
  
    def withdraw(self)
        confirm_withdraw = input("Are you sure you want to withdraw? (yes/no)")
        if confirm_withdraw.lower() == "yes":
            withdraw_amount = float(input("How much would you like to withdraw?"))
            if withdraw_amount > self.balance:
                print("Insufficient funds")
            else:
                self.balance -= withdraw_amount
                print("Withdrawal successful")

bank = BankSystem()
bank.deposit()
bank.withdraw()
                  
     
