
import formulaFunctions as f

def main():
    while True: 
        f.displayMenu()
        userInput = f.getIntegerInput("Enter a number: ")
        f.mathOption(userInput)
        if userInput == 5:
            break
        f.secondaryMenu()



if __name__ == "__main__":
    main()