import random
from termcolor import cprint

QUESTION = "question"
OPTIONS = "options"
ANSWER = "answer"


score_count = 0
quiz = [
    {
        QUESTION: " What is the capital of France?",
        OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        ANSWER: "C",
    },
    {
        QUESTION: " Which planet is know as the red planet?",
        OPTIONS: ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        ANSWER: "B",
    },
    {
        QUESTION: " What is the largest ocean on Earth?",
        OPTIONS: ["A. Atlantic", "B. Indian", "C. Artic", "D. Pacific"],
        ANSWER: "D",
    },
    {
        QUESTION: " Who wrote the play 'Romeo and Juliet'?",
        OPTIONS: [
            "A. William Shakespeare",
            "B. Charles Dickens",
            "C. Mark Twain",
            "D. Jane Austen",
        ],
        ANSWER: "A",
    },
    {
        QUESTION: " What is the chemical symbol for water?",
        OPTIONS: ["A. O2", "B. CO2", "C. H2O", "D. NaCl"],
        ANSWER: "C",
    },
    {
        QUESTION: " How many continents are there on Earth?",
        OPTIONS: ["A. Five", "B. Six", "C. Seven", "D. Eight"],
        ANSWER: "C",
    },
]

random.shuffle(quiz)
for index, item in enumerate(quiz, 1):
    print(f"Question {index}: {item[QUESTION]}")
    for option in item[OPTIONS]:
        print(option)

    answer = input("Your answer: ").upper().strip()

    if answer == item[ANSWER]:
        score_count += 1
        cprint("Correct!", "green")
    else:
        cprint(f"Wrong! The correct answer is {item[ANSWER]}", "red")


print(f"Quiz over! Your final score is {score_count} out of {len(quiz)}")
