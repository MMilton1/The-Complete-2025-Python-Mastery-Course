import random

score_count = 0
quiz = [
    {
        "question": " What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C",
    },
    {
        "question": " Which planet is know as the red planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B",
    },
    {
        "question": " What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Artic", "D. Pacific"],
        "answer": "D",
    },
]

random.shuffle(quiz)
for index, item in enumerate(quiz, 1):
    print(f"Question {index}: {item['question']}")
    for option in item["options"]:
        print(option)

    input("Your answer: ")

# question1 = input(
#     """Question 1: What is the capital of France?
# A. Berlin\nB. Madrid\nC. Paris\nD. Rome\nYour answer: """
# ).upper()

# if question1 == "C":
#     score_count += 1
#     print("Correct!")
# else:
#     print("Wrong! The correct answer is C")

# question2 = input(
#     """Question 2: What planet is known as the red planet?
# A. Earth\nB. Mars\nC. Jupiter\nD. Saturn\nYour answer: """
# ).upper()

# if question2 == "B":
#     score_count += 1
#     print("Correct!")
# else:
#     print("Wrong! The correct answer is B")

# question3 = input(
#     """Question 2: What is the largest ocean on Earth?
# A. Atlantic\nB. Indian\nC. Arctic\nD. Pacific\nYour answer: """
# ).upper()

# if question3 == "D":
#     score_count += 1
#     print("Correct!")
# else:
#     print("Wrong! The correct answer is D")

# print(f"Quiz over! Your final score is {score_count} out of 3")
