# ---------- DO NOT EDIT ------------
import random 
random.seed(256)
# ------------------------------------

def generate_problem(operation: str, difficulty: int) -> int:
    """
    Generates a random math problem (+, -, *, /) based on the given operation and difficulty. The operation is a string that says what operation the problem will be performing.
    The difficulty is from 1-infinity. The more difficult the problem, the bigger the numbers are in the equation.

    Args:
        operation: The type of operation that the problem will generate (addition, subtraction, multiplication, division)
        difficulty: The difficulty for the problem from 1-infinity that determines how big the numbers are.
    
    Returns:
        Prints out a random math problem difficulty
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

    #TODO: Print the operation and return the solution.
    print(f"{first_num} {symbol} {second_num}")

    return answer

def get_valid_operation():
    """
    Generates a random math problem (+, -, *, /) based on the given operation and difficulty. The operation is a string that says what operation the problem will be performing.
    The difficulty is from 1-infinity. The more difficult the problem, the bigger the numbers are in the equation.

    Args:
        operation: The type of operation that the problem will generate (addition, subtraction, multiplication, division)
        difficulty: The difficulty for the problem from 1-infinity that determines how big the numbers are.
    
    Returns:
        Prints out a random math problem difficulty
    """
    valid_ops = ("addition", "subtraction", "multiplication", "division")

    operation = input().strip()


    while operation not in valid_ops: 
        print("Please select either addition, subtraction, multiplication, or division")
        operation = input().strip()
        
    return operation



def get_valid_problem_count(operation):
    """
    Generates a random math problem (+, -, *, /) based on the given operation and difficulty. The operation is a string that says what operation the problem will be performing.
    The difficulty is from 1-infinity. The more difficult the problem, the bigger the numbers are in the equation.

    Args:
        operation: The type of operation that the problem will generate (addition, subtraction, multiplication, division)
        difficulty: The difficulty for the problem from 1-infinity that determines how big the numbers are.
    
    Returns:
        Prints out a random math problem difficulty
    """
    print(f"How many types of {operation} problems would you like to solve?")
    valid_input = False
    num_problems = 0

    while not valid_input:
        try:
            num_problems = int(input().strip())
            if num_problems > 0:
                valid_input = True
            else:
                print("Please enter a number greater than 0!")
        except ValueError:
            print("Please enter a number greater than 0!")
        
    return num_problems
    

# ---------START CODING HERE----------
if __name__ == "__main__":
    
    print("Welcome to Math Quest! Here you will be challenged by answering increasingly difficult math problems until you decide you have had enough.")
    print('You will be presented with n number math problems at a time. If you get more than half right, we will increase the difficulty. Otherwise, we will lower the difficulty, if possible.')    

    difficulty = 1 # starts at 1
    temp_score = 0
    total_questions = 0
    cont = "yep"
    final_score = 0

    while cont != "quit":
        print("Would you like to practice addition, subtraction, multiplication, or division?")
        operation = get_valid_operation()

        num_problems = get_valid_problem_count(operation)

        print(f"Here are your {num_problems} {operation} problems:")

        temp_score = 0        

    
        for i in range(num_problems):
            
            answer = generate_problem(operation, difficulty)
            user_answer = input().strip()

            if user_answer == str(answer):
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
            if difficulty > 1:
                difficulty -= 1
                print(f"Your score was {temp_score}/{num_problems}. We will be lowering the difficulty for next time.")
            else:
                print(f"Your score was {temp_score}/{num_problems}. You are already at the lowest difficulty!")


        print("Continue? (enter 'quit' to exit)")
        cont = input().strip()   



    print(f"Congrats! Your final score was {final_score} out of {total_questions}.")
