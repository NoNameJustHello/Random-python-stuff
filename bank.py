class Bank:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposit successful. New balance: {self.balance}")
    else:
      print("Invalid deposit amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.balance:
      self.balance -= amount
      print(f"Withdrawal successful. New balance: {self.balance}")
    else:
      print("Invalid withdrawal amount or insufficient funds.")
  def check_balance(self):
    print(f"Current balance: {self.balance}")
  def simulation(self,years):
    if years > 0:
      self.balance *= (1 + 0.01) ** years
      print(f"After {years} years, the balance will be: {round(self.balance,2)}")
    else:
      print("Invalid number of years.")
program_is_active = True
user = input("Enter your name: ")
account = Bank(user, 0)
while program_is_active == True:
  print("Welcome to the Bank!")
  print("1. Deposit money")
  print("2. Withdraw money")
  print("3. Check balance")
  print("4. Simulation")
  print("5. Exit")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    amount = float(input("Enter the amount to deposit: "))
    account.deposit(amount)
  elif choice == 2:
    amount = float(input("Enter the amount to withdraw: "))
    account.withdraw(amount)
  elif choice == 3:
    account.check_balance()
  elif choice == 4:
    years = int(input("Enter the number of years: "))
    account.simulation(years)
  elif choice == 5:
    print("Thank you for using the Bank!")
    program_is_active = False  
  else:
    print("Please enter a valid option")