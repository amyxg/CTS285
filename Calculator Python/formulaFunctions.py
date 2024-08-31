def displayMenu():
    """
    Parameters
    ----------
    None.  

    Returns
    -------
    None.
    """
    print("\nWelcome to the calculator program.")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide ")
    print("4. Multiply")
    print("5. Exit")


def getIntegerInput(prompt, minValue, maxValue):
    """
    Parameters
    ----------
    prompt : string
    minValue : int    
    maxValue : int    

    Returns
    -------
    userChoice: int
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
    Parameters
    ----------
    num1 : int
    num2 : int    

    Returns
    -------
    result of the num1 and num2 added
    """
    return num1 + num2

def subtract(num1, num2):
    """
    Parameters
    ----------
    num1 : int
    num2 : int    

    Returns
    -------
    result of the num1 and num2 subtracted
    """
    return num1 - num2

def divide(num1, num2):
    """
    Parameters
    ----------
    num1 : int
    num2 : int    

    Returns
    -------
    result of the num1 and num2 divided
    """
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

def multiply(num1, num2):
    """
    Parameters
    ----------
    num1 : int
    num2 : int    

    Returns
    -------
    result of the num1 and num2 multiplied
    """
    return num1 * num2

# 
def mathOperation(mathChoices, operator):
    """
    Parameters
    ----------
    mathChoices : dictionary
    operator : string    


    Returns
    -------
    None.
    """

    # negative infinity (-inf), positive infinity (inf).. allows user to input any integer from neg to pos.
    num1 = getIntegerInput("Enter the first number: ", float('-inf'), float('inf')) 
    num2 = getIntegerInput("Enter the second number: ", float('-inf'), float('inf'))
    
    result = mathChoices(num1, num2)
    print(f"{num1} {operator} {num2} = {result}")

# determine decision structure for menu choice
def mathOption(userChoice):
    """
    Parameters
    ----------
    userChoice : int

    Returns
    -------
    bool
        DESCRIPTION.
    """
    mathChoices = {
        1: ("Add", add, "+"),
        2: ("Subtract", subtract, "-"),
        3: ("Divide", divide, "/"),
        4: ("Multiply", multiply, "*")
    }
    
    if userChoice in mathChoices:
        print()
        print(mathChoices[userChoice][0]) #prints math Op, ex. "Add"

        # perform mathOperation() as follows for userChoice, ex. if user selected add - call add function and use following string to print 
        mathOperation(mathChoices[userChoice][1], mathChoices[userChoice][2]) 

        return True
    elif userChoice == 5:
        print("Goodbye...")
        return False
    return True

# second menu to determine if user wish to repeat or redirect to main menu
def secondaryMenu():
    """
    Parameters
    ----------
    None.  

    Returns
    -------
    bool
        DESCRIPTION.
    """
    while True:
        print("1. Repeat")
        print("2. Main Menu")
        userSecChoice = getIntegerInput("Enter a number: ", 1, 2)
        
        if userSecChoice == 1:
            return True
        elif userSecChoice == 2:
            return False