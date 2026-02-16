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
    #the key for simble to ensure the math is done correctly in the code for the answer
    if operation == "addition":
        symbol = "+"
    elif operation == "subtraction":
        symbol = "-"
    elif operation == "multiplication":
        symbol = "*"
    elif operation == "division":
        symbol = "/"



    # This will generate a random first and second number for you to use that is multiplied by difficulty 
    first_num = random.randint(1, (10 ** difficulty))
    second_num = random.randint(1, (10 ** difficulty))

    # IF the problem is division, use this code to make the first number the higher one
    if operation == "division": #assigns a max variable to first num and then  the min to second num
        larger = max(first_num, second_num)
        smaller = min(first_num, second_num)
        first_num = larger
        second_num = smaller

    # eval() returns the solution to your problem.
    answer = int(eval(f"{first_num} {symbol} {second_num}"))

    # Print the operation and return the solution.
    print(f"{first_num} {symbol} {second_num}")

    return answer

def get_valid_operation():
    """
    examines +-*/ to determine if the operation selected is cottect

    Args:
        operation: The type of operation that the problem will generate (addition, subtraction, multiplication, division)

    Returns:
        prints the available variables and returns the selected opperation
    """
    valid_ops = ("addition", "subtraction", "multiplication", "division")

    operation = input().strip()


    while operation not in valid_ops: 
        print("Please select either addition, subtraction, multiplication, or division")
        operation = input().strip()
        
    return operation



def get_valid_problem_count(operation):
    """
    accepts the number of problems and makes sure the input is an integer and greater than zero
    Args:
        operation: The type of operation that the problem will generate (addition, subtraction, multiplication, division)
        num_problems: ensures input is integer and greater than zero
    
    Returns:
        Prints out a random math problem difficulty
    """
    print(f"How many types of {operation} problems would you like to solve?")
    
    #baselines
    valid_input = False
    num_problems = 0

    #ensures I only get numbers and uses try so the code does not crash if a letter is entered (Value error)
    while not valid_input:
        try:
            num_problems = int(input().strip())
            if num_problems > 0:
                valid_input = True
            else:
                print("Please enter a number greater than 0!")
        except ValueError:
            print("Please enter a number greater than 0!")
    
    #returns the accurate number of problems
    return num_problems
    

# ---------START CODING HERE----------

if __name__ == "__main__":
    #welcomes user
    print("Welcome to Math Quest! Here you will be challenged by answering increasingly difficult math problems until you decide you have had enough.")
    print('You will be presented with n number math problems at a time. If you get more than half right, we will increase the difficulty. Otherwise, we will lower the difficulty, if possible.')    

    #baseline values for the code so they are defined
    difficulty = 1 # starts at 1
    temp_score = 0
    total_questions = 0
    cont = "yep"
    final_score = 0

    #ensures user does not wish to quit and begins the code by asking the user
    while cont != "quit":
        print("Would you like to practice addition, subtraction, multiplication, or division?")
        operation = get_valid_operation() #recalls the valid operaters

        num_problems = get_valid_problem_count(operation) #recalls the number of problems bring the operator

        print(f"Here are your {num_problems} {operation} problems:") #prints the operations and problems the user will do

        temp_score = 0        

    
        for i in range(num_problems):
            
            answer = generate_problem(operation, difficulty)#recalls generate problems
            user_answer = input().strip()

            if user_answer == str(answer): #checks the user answer
                print("Correct! Next problem...")
                temp_score += 1


            else:
                print("(loud incorrect noise) Wrong! Next problem...")


        #creates a base for scoring
        final_score += temp_score
        total_questions += num_problems

        # checks if they did better than 50% and increases dif
        if temp_score > num_problems / 2:
            difficulty += 1
            print(f"Your score was {temp_score}/{num_problems}. We will be increasing the difficulty for next time!")

        # examines where the dificulty is and lowers it to a min of 1
        elif temp_score <= num_problems:
            if difficulty == 1:
                print(f"Your score was {temp_score}/{num_problems}. You are already at the lowest difficulty!")

            elif difficulty > 1:
                difficulty -= 1
                print(f"Your score was {temp_score}/{num_problems}. We will be lowering the difficulty for next time.")

            else:
                print(f"Your score was {temp_score}/{num_problems}. You are already at the lowest difficulty!")

        #this thing is not working and the lab05b and gradescope are not lineing up
        else:
            print("why am i getting different messages in gradescope")
        
       #asks user if they want to continue
        print("Continue? (enter 'quit' to exit)")
        cont = input().strip().lower()



    #prints final message displaying final score
    print(f"Congrats! Your final score was {final_score} out of {total_questions}.")
