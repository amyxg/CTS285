
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

        // verifies if user entered value is an integer
        int userChoice = checkValidInteger(userInput);

        // determine if user input is between 1-5 with following function to execute, or invalid option
        switch (userChoice){
            case 1:
                System.out.println("\nAdd");
                int[] numbers = getUserIntegers();
                System.out.println(numbers[0] + " + " + numbers[1] + " = " + formula.addNumber(numbers[0], numbers[1]));
                secondaryMenu(userInput, userChoice);
                break;
            /* case 2:
                System.out.println("");
                System.out.println("Add");
                int[] numbers = getUserIntegers();
                System.out.println(numbers[0] + " + " + numbers[1] + " = " + formula.addNumber(numbers[0], numbers[1]));
                secondaryMenu(userInput, userChoice);
                break;
            case 3:
                mathFormula.divideNumber();
                secondaryMenu(userInput, userChoice);
                break;
            case 4:
                mathFormula.multiplyNumber();
                secondaryMenu(userInput, userChoice);
                break; */
            case 5:
                System.out.println ("\nGoodbye.");
                break;
            default:
                // print out error message if not integer between 1-5
                System.out.println("Invalid option. Please select a number between 1-5.\n");
                displayMenu();
                break;
        }
    }

    // get user inputs (two) and put in an array
    public static int[] getUserIntegers(){
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int firstNumber = checkValidInteger(s);
        System.out.print("Enter the second number: ");
        int secondNumber = checkValidInteger(s);

        return new int[]{firstNumber, secondNumber};
    }

    // verifies if user input is an integer
    public static int checkValidInteger(Scanner s) {
        while (!s.hasNextInt()) {
            System.out.print("Invalid input. Please enter an integer: ");
            
            // reads and discards invalid input
            s.next();
        }
        return s.nextInt();
    }

    // display repeat and menu option
    public static void secondaryMenu(Scanner userInput, int initialChoice){
        System.out.println("1. Repeat");
        System.out.println("2. Main Menu");
        System.out.print("Enter a number: ");
        int userChoice = 0;
        // verifies if user entered value is an integer
        while (true) {
            if (userInput.hasNextInt()) {
                while (userChoice != 1 && userChoice != 2) {
                    userChoice = userInput.nextInt();
        
                    switch (userChoice) {
                        case 1:
                            // repeat the operation based on the initial choice
                            switch (initialChoice) {
                                case 1:
                                    System.out.println("");
                                    System.out.println("Add");
                                    int[] numbers = getUserIntegers();
                                    System.out.println(numbers[0] + " + " + numbers[1] + " = " + formula.addNumber(numbers[0], numbers[1]));
                                    secondaryMenu(userInput, initialChoice);
                                    break;
                                /* case 2:
                                    mathFormula.subtractNumber();
                                    break;
                                case 3:
                                    mathFormula.divideNumber();
                                    break;
                                case 4:
                                    mathFormula.multiplyNumber();
                                    break; */
                            }
                            secondaryMenu(userInput, initialChoice);
                            break;
                        case 2:
                            displayMenu();
                            break;
                        default:
                            System.out.print("Invalid option. Please enter 1 or 2: "); //need to ensure they still enter a integer here
                            break;
                    }
                }
                break; 
            } else {
                System.out.print("Invalid option. Please enter an integer: ");
                userInput.next(); 
            }
        }
    }
    
}
