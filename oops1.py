# Initializing a class in python
class employee:
    # initiate the constructor/magic method/ specail method/ dundor method
    def __init__(self, name, age, salary):
        print("Constructor is called")
        self.name = name
        self.age = age
        self.salary = salary
        print("Constructor is executed and the employee details are initialized")

    # method to display employee details
    def display(self):
        print("\nCalling the display method and printing the employee details")
        print(f"Name: {self.name},\nAge: {self.age},\nSalary: {self.salary}")

# initiate an object of the class employee
anil=employee("Anil", 30, 50000)

# call the display method of the object anil
anil.display()

print(type(anil))  # <class '__main__.employee'>