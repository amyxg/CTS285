// This file is for math formula, it requires user input(s)

public class formula {

    // adds two integers 
    public static int addNumber(int firstNumber, int secondNumber){
        return firstNumber + secondNumber;
    }

    // subtracts two integers
    public static int subtractNumber(int firstNumber, int secondNumber){
        return firstNumber - secondNumber;
    }

    // divides two integers 
    public static int divideNumber(int firstNumber, int secondNumber){
        if (firstNumber == 0) {
            System.out.println("Error: Cannot divide by zero.");
            return 0;
        }
        return firstNumber / secondNumber;
    }

    // multiply two integers
    public static int multiplyNumber(int firstNumber, int secondNumber){
        return firstNumber * secondNumber;
    }


}