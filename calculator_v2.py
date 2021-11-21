print("Two Integer Calculator With Four Operations")
print()

def add(x, y):
    print(x + y)

def subtract(x, y):
    print(x - y)

def multiply(x, y):
    print(x * y)

def divide(x, y):
    print(x / y)

while True:

    choice = input("Enter operation (add, subtract, multiply, divide): ")

    if choice in ('add', 'subtract', 'multiply', 'divide'):
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))

    if choice == 'add':
        print(int(num1) + int(num2))

    elif choice == 'subtract':
        print(int(num1) - int(num2))

    elif choice == 'multiply':
        print(int(num1) * int(num2))

    elif choice == 'divide':
        print(int(num1) / int(num2))
    break
else:
    print("Invalid input")