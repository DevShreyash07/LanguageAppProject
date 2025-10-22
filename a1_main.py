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

        # answer user input
        try:
            user_input = int(input("Enter a number: "))
        except Exception:
            print("Invalid input _ counting as wrong. Learn typing first, bro!")
        # Conditions for correct answer
        if user_input < 1 or user_input > len(q["options"]):
            print("Incorrect option bro!")
            progress[modules["title"]]["mistake"] += 1
            progress["TOTAL_SCORE"]["total_mistakes"] += 1
        elif q["options"][user_input - 1] == q["answer"]:
            print("Correct!")
            progress[modules["title"]]["score"] += 1
            progress["TOTAL_SCORE"]["score"] += 1
        else:
            print("Wrong! Correct option is: ", q["answer"])
            progress[modules["title"]]["mistake"] += 1
            progress["TOTAL_SCORE"]["total_mistakes"] += 1
            print()
        print(f"Score: {progress[modules['title']]['score']}, Mistakes: {progress[modules['title']]['mistake']}")
        print("")

def lesson_summary(modules, quiz_level):
    score = progress[modules["title"]]["score"]
    # summary of progress
    total_questions = progress[modules["title"]]["score"] + progress[modules["title"]]["mistake"] # to ensure all questions are counted in a lesson
    total_mistakes = progress["TOTAL_SCORE"]["total_mistakes"]
    correct_answers = score / total_questions * 100

    # printing summary
    print("Progress Summary:\nTotal Questions: ", total_questions)
    print("Overall Score: ", score)
    print("Overall Mistakes: ", total_mistakes)
    print("Total correct questions: ", correct_answers, "%")

    return total_questions, total_mistakes, correct_answers


# Print main info
print("Subject:", lesson_data["subject"])
print("Topic:", lesson_data["topic"], "\n")

# Progress tracker
progress = {"TOTAL_SCORE": {"score": 0, "total_mistakes": 0}}

start_time = time.time()
for idx, modules in enumerate(lesson_data["modules"], start=1):

    # to print lesson name
    print(f"Lesson {idx}. ", modules["title"])

    # progress tracker 
    progress[modules["title"]] = {"score": 0, "mistake": 0}

    # to print lessons
    for i, (marathi, english) in enumerate(modules["lesson"].items(), start=1):
        print(f"{i}. {marathi} - {english}")
    print()

    # for Quiz 1
    while True:
        print("Quiz 1:")
        quiz(modules, "quiz1")
        total_questions, total_mistakes, correct_answers = lesson_summary(modules, "quiz1")

        if correct_answers == 100:
            print("\nCongratulations! You have passed the lesson. \n\nQuiz 2:")
            break # Exit loop 1
        else:
            print("You did not pass the second quiz. I will spank your ass! \nDo it again!\n")
    print("")

    # for Quiz 2
    print("Quiz 2:")
    while True:
        quiz(modules, "quiz2")
        total_questions, total_mistakes, correct_answers = lesson_summary(modules, "quiz2")
        
        if correct_answers == 100:
            print("\nCongratulations! You have passed the lesson.")
            break # Exit loop 1
        else:
            print("You did not pass the second quiz. I will spank your ass! \nDo it again!\n")
    print("")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")
