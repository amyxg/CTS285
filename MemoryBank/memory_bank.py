import time

class MemoryBank:
    """A game where players solve math problems they've stored in a memory bank."""
    
    MAX_PROBLEMS = 10  # Maximum number of problems allowed
    MAX_ATTEMPTS = 2   # Maximum attempts per problem
    
    def __init__(self):
        # List to store math problems
        self.problems = []
        
        # Track game statistics
        self.correct_answers = 0
        self.total_attempts = 0
        self.start_time = 0
        self.end_time = 0
    
    def is_valid_math_problem(self, problem):
        """Check if the math problem is valid.
        
        Args:
            problem (str): The math problem to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Remove spaces and check if problem ends with '='
        problem = problem.strip()
        if not problem.endswith('='):
            print("Problem must end with '=' symbol")
            return False
            
        # Try to solve the math problem to verify it's valid
        try:
            # Remove the '=' and evaluate the expression
            math_expression = problem[:-1]
            eval(math_expression)
            return True
        except:
            print("Invalid math expression. Use only numbers and basic operators (+, -, *, /)")
            return False
    
    def add_problem(self, problem):
        """Add a new math problem to the game.
        
        Args:
            problem (str): The math problem to add
        """
        if len(self.problems) >= self.MAX_PROBLEMS:
            print(f"Memory bank full! Maximum {self.MAX_PROBLEMS} problems allowed.")
            return
            
        if self.is_valid_math_problem(problem):
            problem_data = {
                "question": problem.strip(),
                "is_solved": False,
                "answer": eval(problem[:-1])
            }
            self.problems.append(problem_data)
            print(f"Problem added successfully: {problem}")
    
    def play_game(self):
        """Start the game and let the player solve the problems."""
        if not self.problems:
            print("Please add some math problems first!")
            return
            
        print("\n=== Game Started! ===")
        self.start_time = time.time()
        
        # Go through each problem
        for index, problem in enumerate(self.problems, 1):
            if problem["is_solved"]:
                continue
                
            print(f"\nProblem {index}: {problem['question']}")
            
            # Give player multiple attempts
            for attempt in range(self.MAX_ATTEMPTS):
                try:
                    answer = float(input("Your answer: "))
                    self.total_attempts += 1
                    
                    if answer == problem["answer"]:
                        print("✓ Correct!")
                        problem["is_solved"] = True
                        self.correct_answers += 1
                        break
                    else:
                        remaining = self.MAX_ATTEMPTS - attempt - 1
                        if remaining > 0:
                            print(f"✗ Wrong answer. You have {remaining} more attempt(s).")
                        else:
                            print(f"✗ Wrong answer. The correct answer was: {problem['answer']}")
                except ValueError:
                    print("Please enter a valid number.")
                    
        self.end_time = time.time()
        self.show_results()
    
    def show_results(self):
        """Display the game results."""
        time_taken = round(self.end_time - self.start_time, 1)
        
        print("\n=== Game Results ===")
        print(f"Correct Answers: {self.correct_answers}")
        print(f"Total Attempts: {self.total_attempts}")
        print(f"Time Taken: {time_taken} seconds")
        
        # Calculate and show success rate
        success_rate = (self.correct_answers / len(self.problems)) * 100
        print(f"Success Rate: {success_rate:.1f}%")

def main():
    # Create new game
    game = MemoryBank()
    
    # Instructions
    print("Welcome to MathZebra Memory Game!")
    print("Enter up to 10 math problems. Each problem should end with '='")
    print("Example: 2 + 2 =\n")
    
    # Collect problems from user
    while len(game.problems) < MemoryBank.MAX_PROBLEMS:
        problem = input(f"Enter problem {len(game.problems) + 1} (or press Enter to start): ")
        
        if not problem:  # Empty input
            if game.problems:  # If we have at least one problem, start the game
                break
            print("Please add at least one problem!")
            continue
            
        game.add_problem(problem)
    
    # Start the game
    input("\nPress ENTER when you're ready to solve the problems...")
    game.play_game()

if __name__ == "__main__":
    main()