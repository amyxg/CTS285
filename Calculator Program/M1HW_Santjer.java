
import java.util.Scanner;

public class M1HW_Santjer {
    public static void main(String[] args) {
        displayMenu();
    }

    // displays menu option for user
    public static void displayMenu(){
        System.out.println("\nWelcome to the calculator program.");
        System.out.println("1. Add");
        System.out.println("2. Subtract");
        System.out.println("3. Divide");
        System.out.println("4. Multiply");
        System.out.println("5. Exit");
        System.out.print("Enter a number: ");
        Scanner userInput = new Scanner(System.in);
        int userChoice = userInput.nextInt();

        // determine if user input is between 1-5 with following function to execute, or invalid option
        switch (userChoice){
            case 1:
                addNumber();
                secondaryMenu(userInput, userChoice);
                break;
            case 2:
                subtractNumber();
                secondaryMenu(userInput, userChoice);
                break;
            case 3:
                divideNumber();
                secondaryMenu(userInput, userChoice);
                break;
            case 4:
                multiplyNumber();
                secondaryMenu(userInput, userChoice);
                break;
            case 5:
                System.out.println("");
                System.out.println ("Goodbye.");
                break;
            default:
                // print out error message if not integer between 1-5
                System.out.println("");
                System.out.println("Invalid option. Please select a number between 1-5.");
                System.out.println("");
                displayMenu();
                break;
        }
    }

    // verifies if user input is an integer
    public static int checkValidInteger(Scanner s, String prompt) {
        System.out.print(prompt);
        while (!s.hasNextInt()) {
            System.out.println("Invalid input. Please enter a valid integer.");
            
            // reads and discards invalid input
            s.next(); 

            System.out.print(prompt);
        }
        return s.nextInt();
    }


    // display repeat and menu option
    public static void secondaryMenu(Scanner userInput, int initialChoice){
        System.out.println("1. Repeat");
        System.out.println("2. Main Menu");
        System.out.print("Enter a number: ");
        int userChoice = 0;

        while (userChoice != 1 && userChoice != 2) {
            userChoice = userInput.nextInt();

            switch (userChoice) {
                case 1:
                    // repeat the operation based on the initial choice
                    switch (initialChoice) {
                        case 1:
                            addNumber();
                            break;
                        case 2:
                            subtractNumber();
                            break;
                        case 3:
                            divideNumber();
                            break;
                        case 4:
                            multiplyNumber();
                            break;
                    }
                    secondaryMenu(userInput, initialChoice);
                    break;
                case 2:
                    displayMenu();
                    break;
                default:
                    System.out.println("Invalid option. Please enter 1 or 2.");
                    break;
            }
        }
    }

    // adds two integers and display results
    public static void addNumber(){
        Scanner s = new Scanner(System.in);
        System.out.println("");
        System.out.println("Add");
        int firstNumber = checkValidInteger(s, "Enter the a number: ");
        int secondNumber = checkValidInteger(s, "Enter the another number: ");
        //results
        System.out.println(firstNumber + " + " + secondNumber + " = " + (firstNumber + secondNumber));
    }

    // subtract two integers and display results
    public static void subtractNumber(){
        Scanner s = new Scanner(System.in);
        System.out.println("");
        System.out.println("Subtract");
        int firstNumber = checkValidInteger(s, "Enter the a number: ");
        int secondNumber = checkValidInteger(s, "Enter the another number: ");
        //results
        System.out.println(firstNumber + " - " + secondNumber + " = " + (firstNumber - secondNumber));
    }

        // divide two integers and display results (as a decimal)
        public static void divideNumber(){
            Scanner s = new Scanner(System.in);
            System.out.println("");
            System.out.println("Divide");
            int firstNumber = checkValidInteger(s, "Enter the a number: ");
            int secondNumber = checkValidInteger(s, "Enter the another number: ");
            //results
            System.out.println(firstNumber + " / " + secondNumber + " = " + ((double)firstNumber / secondNumber));
        }

        // multiply two integers and display results
        public static void multiplyNumber(){
            Scanner s = new Scanner(System.in);
            System.out.println("");
            int firstNumber = checkValidInteger(s, "Enter the a number: ");
            int secondNumber = checkValidInteger(s, "Enter the another number: ");
            //results
            System.out.println(firstNumber + " x " + secondNumber + " = " + (firstNumber * secondNumber));
        }
}
