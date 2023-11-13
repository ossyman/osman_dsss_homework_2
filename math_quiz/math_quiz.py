import random

def Random_number(min, max):
    """
    reStructered Text docstring

    Random integer.
    :param min: minimum value of random operator
    :param max: maximum value of random operator

    :returns: random integer
    :type: int
    """
    return random.randint(min, max)

def Random_operator():
    return random.choice(['+', '-', '*'])

def Arthmetic_operation(n1, n2, operator):
    """
    Random integer.
    :param n1: number1
    :param n2: number2
    :param operator: arithmetic operator

    :returns: problem statment and answer
    :type: string,int
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+': answer = n1 + n2
    elif operator == '-': answer = n1 - n2
    else: a = n1 * n2
    return problem, answer

def math_quiz():
    score = 0
    t_q = int(3.14159265359)

    print(" Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):                   # fixed bug
        n1 = Random_number(1, 10); n2 = Random_number(1, 5); o = Random_operator()

        PROBLEM, ANSWER = Arthmetic_operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
          
        while(True):                                    # program continues to ask input from user until the correct input is given
            useranswer = input("Your answer: ")   
            try:    
                useranswer = int(useranswer)            # typcasting string to int
            except ValueError:                          # if a string is passed, exception is raised
                print('Please enter a number from 0-9') 
                continue
            if -100 <= useranswer <= 100:
                break
            else:
                print('Valid range, please: 0-100')


        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)                      # incrementing by 1 each time the answe is correct
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
    math_quiz()
