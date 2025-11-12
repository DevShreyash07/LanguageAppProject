import a2_data
import a3_feedbackmode
import random
import time

# import data
lesson_data = a2_data.lesson_data
MODE = a3_feedbackmode.MODE
RESPONSES = a3_feedbackmode.RESPONSES

# Quiz questions, options, user input, answers, feedback and question scoring function
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
            answer_result = "incorrect option"
            quiz_progress[modules["title"]]["quiz_mistakes"] += 1
            lesson_progress["LESSON_SCORE"]["lesson_mistakes"] += 1
        elif q["options"][user_input - 1] == q["answer"]:
            answer_result = "correct answer"
            quiz_progress[modules["title"]]["quiz_score"] += 1
            lesson_progress["LESSON_SCORE"]["lesson_score"] += 1
        else:
            answer_result = "incorrect answer"
            quiz_progress[modules["title"]]["quiz_mistakes"] += 1 
            lesson_progress["LESSON_SCORE"]["lesson_mistakes"] += 1
        
        print(feedback_mode("questions_feedback", answer_result))
        print(f"Score: {quiz_progress[modules['title']]['quiz_score']}, Mistakes: {quiz_progress[modules['title']]['quiz_mistakes']}\n")


# Lesson summary function
def lesson_summary(modules):
    total_questions = quiz_progress[modules["title"]]["quiz_score"] + quiz_progress[modules["title"]]["quiz_mistakes"]
    total_score = quiz_progress[modules["title"]]["quiz_score"]
    total_mistakes = quiz_progress[modules["title"]]["quiz_mistakes"]
    correct_answers = total_score / total_questions * 100 if total_questions > 0 else 0

    print("Progress Summary: ")
    print(f"Total Questions: {total_questions}")
    print(f"Quiz Score: {total_score}")
    print(f"Quiz Mistakes: {total_mistakes}")
    print(f"Correct Answers: {correct_answers:.2f}%\n")

    feedback = "passed" if correct_answers == 100 else "failed"

    print(feedback_mode("lesson_feedback", feedback))

    return total_questions, total_mistakes, correct_answers


# Feedback mode function
def feedback_mode(response_type: str, feedback_type: str):
    """
    response_type: 'questions_feedback', 'quiz_feedback', 'lesson_feedback',
    feedback_type: 'correct answer', 'incorrect answer', 'incorrect option', 'passed', 'failed',
    """

    select_mode = random.choice(MODE)

    if response_type not in RESPONSES:
        return "no value bro!"
    if feedback_type not in RESPONSES[response_type]:
        return "nahi milega!"
    
    return random.choice(RESPONSES[response_type][feedback_type][select_mode])
    
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

        quiz_data = quiz(modules, "quiz1")
        _, _, correct_answers = lesson_summary(modules)

        if correct_answers == 100:
            print("Congrats! Passed Quiz 1.\n")
            print(feedback_mode("questions_feedback", "passed"))
            break
        else:
            print("You did not pass Quiz 1. Try again!\n")
            print(feedback_mode("questions_feedback", "failed"))
            # reset quiz progress only
            quiz_progress[modules["title"]] = {"quiz_score": 0, "quiz_mistakes": 0}

    # Quiz 2
    while True:
        print("Quiz 2:")

        quiz_data = quiz(modules, "quiz2")
        _, _, correct_answers = lesson_summary(modules)

        if correct_answers == 100:
            print("Congrats! Passed Quiz 2.\n")
            print(feedback_mode("questions_feedback", "passed"))
            break
        else:
            print("You did not pass Quiz 2. Try again!\n")
            print(feedback_mode("questions_feedback", "failed"))
            # reset quiz progress only
            quiz_progress[modules["title"]] = {"quiz_score": 0, "quiz_mistakes": 0}

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")
