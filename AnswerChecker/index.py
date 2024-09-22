def calculate_answer(firstNum, mathOp, secondNum):
    """
    firstNum: float
    mathOp: string
    secondNum: float

    performs math operation depending on var MathOp string value
    """
    if mathOp == '+':
        return firstNum + secondNum
    elif mathOp == '-':
        return firstNum - secondNum
    elif mathOp == '/':
        return firstNum / secondNum
    elif mathOp == '*':
        return firstNum * secondNum
    else:
        return None  # In case of an invalid operator
    

def main():
    print("Welcome to the Answer Checker!\nI check your math answers for you!\n")
    correct_count = 0  # Initialize correct answer counter
    total_attempts = 0  # Initialize total problems attempted

    # loop to check math answers continuously if input = yes
    while True:
        firstNum = float(input("Enter your first number: "))  # First number to use in math problem
        mathOp = input("Enter a math symbol (Example: +, -, /, *): ")  # Math operator
        secondNum = float(input("Enter your second number: "))  # Second number to use in math problem

        correctAnswer = calculate_answer(firstNum, mathOp, secondNum)
        
        if correctAnswer is None:
            print("Invalid math operator! Please restart the program.")
            continue  # Skip this loop iteration if the operator is invalid
        
        attempts = 0  # Initialize the attempt counter for this problem
        user_correct = False  # Track if the user gets the correct answer for this problem

        # Loop, only gives user 2 attempts to solve math problems correctly
        while attempts < 2:
            userAnswer = float(input("Enter your answer: ")) 
            
            if userAnswer == correctAnswer:
                print("Correct! Great job!")
                correct_count += 1  # Increment correct answers count
                user_correct = True
                break  # Exit the loop when the user gives the correct answer
            else:
                attempts += 1
                if attempts < 2:
                    print("Incorrect. Try again!")

        if not user_correct:
            print(f"Sorry, the correct answer is: {correctAnswer}")

        total_attempts += 1  # Increment total problems attempted

        # Ask user if they want to continue
        continue_checker = input("Do you want to try another problem? (yes/no): ").lower()

        if continue_checker != 'yes':
            break  # Exit the loop if the user doesn't want to continue

    # Display final score
    print(f"\nYou answered {correct_count} problems correctly.")
    print(f"You attempted {total_attempts} problems in total.")

if __name__ == "__main__":
    main()