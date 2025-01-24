import random
from termcolor import cprint


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

    answer = input("Your answer: ").upper().strip()

    if answer == item["answer"]:
        score_count += 1
        cprint("Correct!", "green")
    else:
        cprint(f"Wrong! The correct answer is {item['answer']}", "red")


print(f"Quiz over! Your final score is {score_count} out of {len(quiz)}")
