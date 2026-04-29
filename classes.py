class person:
    def __init__(self,name,age,address,email):
        self.name = name
        self.address = address
        self.age =age
        self.email = email

    def talks(self):
        print(f"{self.name} is talking")

    def walks(self):
        print(f'{self.name}is walking')

person1 = person('mike',24,'karen','mike@gmail.com')
print(type(person1))
print(person1.name)
person1.talks()

person2=person('ruth',23,'langata','ruth@gmail.com')
print(type(person2))
print(person2.address)

class BankAccount:
    def __init__(self, account_number, balance, name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.name = name
        self.date_opened = date_opened

    def deposit(self, amount):
        self.balance=self.balance + amount
        print(f'{self.name} deposited {amount}')
        return f'{self.name} deposited {amount} new balance:{self.balance}'

    def withdraw(self, amount):
        self.balance=self.balance - amount
        print(f'{self.name} withdrew {amount}')
        return f'{self.name} withdrew {amount} new balance:{self.balance}'


acc1 = BankAccount("1001", 5000, "Larry", "2023-04-17")
print (acc1.deposit(1500))
print(acc1.withdraw(2000))


acc2 = BankAccount("1002", 3000, "Mary", "2023-04-17")
print(acc2.deposit(1000))
print(acc2.withdraw(500))


class Car:
    def __init__(self, brand, model, year, fuel_capacity, fuel_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.is_running = False  
    
    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            return f"{self.brand} {self.model} has started."
        return "Cannot start. No fuel."

    def stop(self):
        self.is_running = False
        return f"{self.brand} {self.model} has stopped."

    def refuel(self, amount):
        if amount <= 0:
            return "Invalid fuel amount"

        if self.fuel_level + amount > self.fuel_capacity:
            self.fuel_level = self.fuel_capacity
            return "Tank is full"

        self.fuel_level += amount
        return f"Refueled {amount}L. Current fuel: {self.fuel_level}L"
    
    def drive(self, distance):
        if not self.is_running:
            return "Start the car first"

        fuel_needed = distance * 0.1  

        if fuel_needed > self.fuel_level:
            return "Not enough fuel to drive that distance"

        self.fuel_level -= fuel_needed
        return f"Drove {distance}km. Fuel left: {self.fuel_level}L"


    def display_car_info(self):
        return f"""
Brand: {self.brand}
Model: {self.model}
Year: {self.year}
Fuel Capacity: {self.fuel_capacity}
Fuel Level: {self.fuel_level}
Is Running: {self.is_running}
"""
car = Car("subaru", "audi", 2026, 50, 20)

print(car.display_car_info())

print(car.start())
print(car.drive(50))
print(car.refuel(10))
print(car.drive(100))
print(car.stop())

print(car.display_car_info())