import a2_data
import time

# import data
lesson_data = a2_data.lesson_data

def quiz(modules, quiz_level):
    for i, q in enumerate(modules["quiz_section"][quiz_level], start=1):
        print(f"Q{i}. ", q["question"])

        # options
        for idx_opt, opt in enumerate(q["options"], start=1):
            print(f"{idx_opt}. ", opt)

        # user input
        try:
            user_input = int(input("Enter a number: "))
        except Exception:
            print("Invalid input _ counting as wrong. Learn typing first bro!")
            user_input = -1  # force as wrong

        # conditions
        if user_input < 1 or user_input > len(q["options"]):
            print("Incorrect option bro!")
            quiz_progress[modules["title"]]["quiz_mistakes"] += 1
            lesson_progress["LESSON_SCORE"]["lesson_mistakes"] += 1
        elif q["options"][user_input - 1] == q["answer"]:
            print("Correct!")
            quiz_progress[modules["title"]]["quiz_score"] += 1
            lesson_progress["LESSON_SCORE"]["lesson_score"] += 1
        else:
            print("Wrong! Correct option is: ", q["answer"])
            quiz_progress[modules["title"]]["quiz_mistakes"] += 1
            lesson_progress["LESSON_SCORE"]["lesson_mistakes"] += 1

        print(f"Score: {quiz_progress[modules['title']]['quiz_score']}, Mistakes: {quiz_progress[modules['title']]['quiz_mistakes']}\n")


def lesson_summary(modules):
    total_questions = quiz_progress[modules["title"]]["quiz_score"] + quiz_progress[modules["title"]]["quiz_mistakes"]
    total_score = quiz_progress[modules["title"]]["quiz_score"]
    total_mistakes = quiz_progress[modules["title"]]["quiz_mistakes"]
    correct_answers = total_score / total_questions * 100 if total_questions > 0 else 0

    print("Progress Summary:")
    print(f"Total Questions: {total_questions}")
    print(f"Quiz Score: {total_score}")
    print(f"Quiz Mistakes: {total_mistakes}")
    print(f"Correct Answers: {correct_answers:.2f}%\n")

    return total_questions, total_mistakes, correct_answers


# Main info
print("Subject:", lesson_data["subject"])
print("Topic:", lesson_data["topic"], "\n")

# Lesson progress tracker
lesson_progress = {"LESSON_SCORE": {"lesson_score": 0, "lesson_mistakes": 0}}

start_time = time.time()

for idx, modules in enumerate(lesson_data["modules"], start=1):
    print(f"Lesson {idx}. ", modules["title"])

    # Quiz progress tracker
    quiz_progress = {}
    quiz_progress[modules["title"]] = {"quiz_score": 0, "quiz_mistakes": 0}

    # Print lessons
    for i, (marathi, english) in enumerate(modules["lesson"].items(), start=1):
        print(f"{i}. {marathi} - {english}")
    print()

    # Quiz 1
    while True:
        print("Quiz 1:")
        quiz(modules, "quiz1")
        _, _, correct_answers = lesson_summary(modules)

        if correct_answers == 100:
            print("Congrats! Passed Quiz 1.\n")
            break
        else:
            print("You did not pass Quiz 1. Try again!\n")
            # reset quiz progress only
            quiz_progress[modules["title"]] = {"quiz_score": 0, "quiz_mistakes": 0}

    # Quiz 2
    while True:
        print("Quiz 2:")
        quiz(modules, "quiz2")
        _, _, correct_answers = lesson_summary(modules)

        if correct_answers == 100:
            print("Congrats! Passed Quiz 2.\n")
            break
        else:
            print("You did not pass Quiz 2. Try again!\n")
            # reset quiz progress only
            quiz_progress[modules["title"]] = {"quiz_score": 0, "quiz_mistakes": 0}

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")
