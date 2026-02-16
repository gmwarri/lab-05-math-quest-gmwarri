# ---------- DO NOT EDIT ------------
import random 
random.seed(256)
# ------------------------------------


def generate_problem(operation: str, difficulty: int) -> int:
    """
    Generate a random math problem based on operation and difficulty.
    """
    if operation == "addition":
        symbol = "+"
    elif operation == "subtraction":
        symbol = "-"
    elif operation == "multiplication":
        symbol = "*"
    elif operation == "division":
        symbol = "/"
    
    # This will generate a random first and second number for you to use
    first_num = random.randint(1, (10 ** difficulty))
    second_num = random.randint(1, (10 ** difficulty))

    # IF the problem is division, use this code to make the first number the higher one
    if operation == "division":
        larger = max(first_num, second_num)
        smaller = min(first_num, second_num)
        first_num = larger
        second_num = smaller

    # eval() returns the solution to your problem.
    answer = int(eval(f"{first_num} {symbol} {second_num}"))
    #Print the operation and return the solution.
    print(f"{first_num} {symbol} {second_num}")
    return answer


def get_valid_operation():
    """
    Prompts and validates the math operation input.
    """
    valid_ops = ("addition", "subtraction", "multiplication", "division")
    operation = input().strip()

    while operation not in valid_ops: 
        print("Please select either addition, subtraction, multiplication, or division")
        operation = input().strip()
    return operation

def get_valid_problem_count(operation):
    """
    Prompts and validates the number of problems (must be > 0).
    """
    print(f"How many types of {operation} problems would you like to solve?")
    valid_input = False
    num_problems = 0
    while not valid_input:
        user_input = input().strip()
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            num_problems = int(user_input)
            if num_problems > 0:
                valid_input = True
            else:
                print("Please enter a number greater than 0!")
        else:
            print("Please enter a number greater than 0!")
    return num_problems

# ---------START CODING HERE----------
if __name__ == "__main__":
    print("Welcome to Math Quest! Here you will be challenged by answering increasingly difficult math problems until you decide you have had enough.")
    print("You will be presented with n number math problems at a time. If you get more than half right, we will increase the difficulty. Otherwise, we will lower the difficulty, if possible.")    

    difficulty = 1 
    total_questions = 0
    final_score = 0
    keep_playing = True

    while keep_playing:
        print("Would you like to practice addition, subtraction, multiplication, or division?")
        operation = get_valid_operation()
        num_problems = get_valid_problem_count(operation)

        print(f"Here are your {num_problems} {operation} problems:")
        temp_score = 0        
    
        for i in range(num_problems):
            answer = generate_problem(operation, difficulty)
            user_input = input().strip()
            
            if user_input.lstrip('-').isdigit() and int(user_input) == answer:
                print("Correct! Next problem...")
                temp_score += 1
            else:
                print("(loud incorrect noise) Wrong! Next problem...")

        final_score += temp_score
        total_questions += num_problems

        if temp_score > num_problems / 2:
            difficulty += 1
            print(f"Your score was {temp_score}/{num_problems}. We will be increasing the difficulty for next time!")
        else:
            if difficulty == 1:
                print(f"Your score was {temp_score}/{num_problems}. You are already at the lowest difficulty!")
            else:
                difficulty -= 1
                print(f"Your score was {temp_score}/{num_problems}. We will be lowering the difficulty for next time.")

        print("Continue? (enter 'quit' to exit)")
        cont_choice = input().strip().lower()
        if cont_choice == "quit":
            keep_playing = False

