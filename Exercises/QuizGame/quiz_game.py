import random
from termcolor import cprint

QUESTION = "question"
OPTIONS = "options"
ANSWER = "answer"


score_count = 0


def ask_question(index, question, options):
    print(f"Question {index}: {question}")
    for option in options:
        print(option)

    return input("Your answer: ").upper().strip()


def run_quiz(quiz):
    random.shuffle(quiz)
    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION], item[ANSWER])

    if answer == item[ANSWER]:
        score_count += 1
        cprint("Correct!", "green")
    else:
        cprint(f"Wrong! The correct answer is {item[ANSWER]}", "red")

    print(f"Quiz over! Your final score is {score_count} out of {len(quiz)}")


def main():
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
    run_quiz(quiz)


if __name__ == "main":
    main()
