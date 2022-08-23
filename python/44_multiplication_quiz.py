# Multiplication quiz program using pyinputplus
import pyinputplus as pyip
import random
import time

num_of_questions = 10
correct_answers = 0

# Pick two random number and show prompt to the user
for question_num in range(num_of_questions):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    user_prompt = f"#{question_num + 1}: {num_1} x {num_2} = "

    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handled by blockRegexes with a custom message
        pyip.inputStr(user_prompt, allowRegexes=[
                      f"^{num_1 * num_2}$"], blockRegexes=[(".*", "Incorrect!")], timeout=8, limit=3)
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries")
    else:
        # This block of code run if no exception were raised in the try block
        print("Correct!")
        correct_answers += 1

    # Brief pause to let user see the result
    time.sleep(1)

print(f"Score: {correct_answers} out of {num_of_questions}")
