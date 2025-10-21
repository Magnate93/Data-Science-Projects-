# Question 1: Create a class named Car with the attributes brand, model, and year. 
# Include a constructor to initialize these values and a method display_info() to print all the car details. 
# Then create an object of the Car class and display its details.

class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information:\n  Brand: {self.brand}\n  Model: {self.model}\n  Year: {self.year}")

car = Car("Toyota", "Camry", 2020)
car.display_info()

# Question 2: Create three classes Animal, Mammal, and Dog where Animal has a method eat(), Mammal inherits from Animal 
# and has a method walk(), and Dog inherits from Mammal and has a method bark(). 
# Create an object of Dog and demonstrate all three methods. Also, create a class Calculator with an add() method 
# that can take either two or three parameters, and then create a subclass AdvancedCalculator 
# that overrides the add() method to add any number of parameters using variable-length arguments. 
# Demonstrate both functionalities.

class Animal:
    def eat(self):
        print("Animal is eating")

class Mammal(Animal):
    def walk(self):
        print("Mammal is walking")

class Dog(Mammal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()  
dog.walk()  
dog.bark()  

class Calculator:
    def add(self, a, b):
        return a + b

class AdvancedCalculator(Calculator):
    def add(self, *args):
        total = sum(args)
        return total

calc = Calculator()
print("Calculator add(2, 3):", calc.add(2, 3))  

adv_calc = AdvancedCalculator()
print("AdvancedCalculator add(1, 2, 3, 4):", adv_calc.add(1, 2, 3, 4))  
print("AdvancedCalculator add(5, 10):", adv_calc.add(5, 10))        

# Question 3: Create a class BankAccount with a private attribute balance and provide methods deposit() and withdraw() to modify 
# the balance safely so that the balance cannot be accessed directly. Then create two subclasses SavingsAccount and CurrentAccount, 
# each having a method account_type() that prints its respective account type. 
# Demonstrate polymorphism by calling account_type() from different account objects.

class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.__balance = float(initial_balance)  # private attribute

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self): 
        return self.__balance

class SavingsAccount(BankAccount):
    def account_type(self):
        print("Savings Account")

class CurrentAccount(BankAccount):
    def account_type(self):
        print("Current Account")

accounts = [
    SavingsAccount(1000),
    CurrentAccount(500)
]

for acc in accounts:
    acc.account_type()

sa = SavingsAccount(100)
sa.deposit(50)
sa.withdraw(30)
print("SavingsAccount balance after transactions:", sa.get_balance())

ca = CurrentAccount(200)
ca.deposit(100)
ca.withdraw(50)
print("CurrentAccount balance after transactions:", ca.get_balance())