// This file is for math formula, it requires user input(s)
public class mathFormula {
// adds two integers and display results
public static void addNumber(){
    Scanner s = new Scanner(System.in);
    System.out.println("");
    System.out.println("Add");
    int firstNumber = checkValidInteger(s, "Enter a number: ");
    int secondNumber = checkValidInteger(s, "Enter another number: ");
    //results
    // instead of (firstNumber + secondNumber), should be something like add(firstNumber, secondNumber) in a different class
    System.out.println(firstNumber + " + " + secondNumber + " = " + (firstNumber + secondNumber));
}

// subtract two integers and display results
public static void subtractNumber(){
    Scanner s = new Scanner(System.in);
    System.out.println("");
    System.out.println("Subtract");
    int firstNumber = checkValidInteger(s, "Enter a number: ");
    int secondNumber = checkValidInteger(s, "Enter another number: ");
    //results
    System.out.println(firstNumber + " - " + secondNumber + " = " + (firstNumber - secondNumber));
}

    // divide two integers and display results (as a decimal)
    public static void divideNumber(){
        Scanner s = new Scanner(System.in);
        System.out.println("");
        System.out.println("Divide");
        int firstNumber = checkValidInteger(s, "Enter a number: ");
        int secondNumber = checkValidInteger(s, "Enter another number: ");
        //results
        System.out.println(firstNumber + " / " + secondNumber + " = " + ((double)firstNumber / secondNumber));
    }

    // multiply two integers and display results
    public static void multiplyNumber(){
        Scanner s = new Scanner(System.in);
        System.out.println("");
        int firstNumber = checkValidInteger(s, "Enter a number: ");
        int secondNumber = checkValidInteger(s, "Enter another number: ");
        //results
        System.out.println(firstNumber + " x " + secondNumber + " = " + (firstNumber * secondNumber));
    }
}