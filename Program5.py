class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


name = input("Enter your name: ")
balance = float(input("Enter initial balance: "))

customer = Bank(name, balance)

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        customer.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        customer.withdraw(amount)

    elif choice == 3:
        customer.display()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")