
import formulaFunctions as f

def main():
    while True: 
        f.displayMenu()

        # get only valid numbers from 1 to 5
        userInput = f.getIntegerInput("Enter a number: ", 1, 5)

        while True:
            # if user chose to exit (5), exit 
            if not f.mathOption(userInput):
                return
            #if user chose 2 in secondary menu, break the inner loop to return to the main menu (main())
            if not f.secondaryMenu():
                break



if __name__ == "__main__":
    main()