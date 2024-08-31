def displayMenu():
    """
    displays a menu option 1-5
    """
    print("Welcome to the calculator program.")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide ")
    print("4. Multiply")
    print("5. Exit")


def getIntegerInput(prompt, minValue, maxValue):
    """
    returns an integer or error message 
    """
    while True:
        try:
            userChoice = int(input(prompt))
            if minValue <= userChoice <= maxValue:
                return userChoice
            else:
                print(f"Please enter a number between {minValue} and {maxValue}.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# math formulas
def add(num1, num2):
    """
    num1: int 
    num2: int
    """
    return num1 + num2

def subtract(num1, num2):
    """
    num1: int 
    num2: int
    """
    return num1 - num2

def divide(num1, num2):
    """
    num1: int 
    num2: int
    """
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

def multiply(num1, num2):
    """
    num1: int 
    num2: int
    """
    return num1 * num2

# 
def mathOperation(mathChoices, operator):
    """
    mathChoices: a dictionary
    operator: string
    """
    num1 = getIntegerInput("Enter the first number: ", float('-inf'), float('inf')) # negative infinity (-inf), positive infinity (inf).. allows user to input any integer from neg to pos.
    num2 = getIntegerInput("Enter the second number: ", float('-inf'), float('inf'))
    
    result = mathChoices(num1, num2)
    print(f"{num1} {operator} {num2} = {result}")

# determine decision structure for menu choice
def mathOption(userChoice):
    """
    userChoice: int 
    """
    operations = {
        1: ("Add", add, "+"),
        2: ("Subtract", subtract, "-"),
        3: ("Divide", divide, "/"),
        4: ("Multiply", multiply, "*")
    }
    
    if userChoice in operations:
        print(operations[userChoice][0])
        mathOperation(operations[userChoice][1], operations[userChoice][2])
        return True
    elif userChoice == 5:
        print("Goodbye...")
        return False
    return True

# second menu to determine if user wish to repeat or redirect to main menu
def secondaryMenu():
    while True:
        print("1. Repeat")
        print("2. Main Menu")
        userSecChoice = getIntegerInput("Enter a number: ", 1, 2)
        
        if userSecChoice == 1:
            return True
        elif userSecChoice == 2:
            return False