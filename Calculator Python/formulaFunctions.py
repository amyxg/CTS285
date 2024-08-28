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


def checkValidInteger(userChoice):
    """
    returns integer value or None if not valid 
    """
    if userChoice.isdigit():
        return int(userChoice)
    else:
        return None


def getIntegerInput(prompt):
    """
    returns an integer or error message 
    """
    while True:
        userChoice = input(prompt)
        choice = checkValidInteger(userChoice)
        if choice is not None:
            return choice
        else: 
            print("Invalid option! Please enter a number") 


# determine decision structure for menu choice
def mathOption(userChoice):
    match userChoice:
        case 1:
            add(num1, num2)
        case 2: 
            subtract(num1, num2)
        case 3:
            divide(num1, num2)
        case 4:
            multiply(num1, num2)
        case 5:
            print("Goodbye...")    
        case _:
            # this is the default handler if none of the abvoe cases match
            print("Invalid option! Please enter a number from 1 to 5.")

# math formulas
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

# second menu to determine if user wish to repeat or redirect to menu
def secondaryMenu(userChoice, userSecChoice):
    print("1. Repeat")
    print("2. Main Menu")
    match userSecChoice:
        case 1:
            mathOption(userChoice)
            print("repeat option")
        case 2: 
            displayMenu()  
        case _:
            # this is the default handler if none of the abvoe cases match
            print("ERROR! PLease enter a number from 1 to 2. ")