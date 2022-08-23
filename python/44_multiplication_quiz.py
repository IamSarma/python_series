# Multiplication quiz program using pyinputplus
import pyinputplus
import random
import time

num_of_questions = 10
correct_answers = 0

# Pick two random number and show prompt to the user
for question_num in range(num_of_questions):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    user_prompt = f"#{question_num + 1}: {num_1} x {num_2} = "
    print(user_prompt)
