import a2_data
import time

# import data
lesson_data = a2_data.lesson_data

# Print main info
print("Subject:", lesson_data["subject"])
print("Topic:", lesson_data["topic"], "\n")

# Progress tracker
progress = {"TOTAL_SCORE": {"total_score": 0, "total_mistakes": 0}}

start_time = time.time()
for idx, modules in enumerate(lesson_data["modules"], start=1):
    # to print lesson name
    print(f"Lesson {idx}. ", modules["title"])

    # progress tracker for each module
    progress[modules["title"]] = {"score": 0, "mistakes": 0}

    # to print lessons
    for i, (marathi, english) in enumerate(modules["lesson"].items(), start=1):
        print(f"{i}. {marathi} - {english}")
    print()
    # quiz
    for quiz_level in ["quiz1", "quiz2"]:
        for i, q in enumerate(modules["quiz_level"], start=1):
            print(f"Q{i}. ", q["question"])
        # options
        for idx_opt, opt in enumerate(q["options"], start=1):
            print(f"{idx_opt}. ", opt)
        # answer
        user_input = int(input("Enter a number: "))
        if user_input < 1 or user_input > len(q["options"]):
            print("Incorrect option bro!")
            progress[modules["title"]]["mistakes"] += 1
            progress["TOTAL_SCORE"]["total_mistakes"] += 1
        elif q["options"][user_input - 1] == q["answer"]:
            print("Correct!")
            progress[modules["title"]]["score"] += 1
            progress["TOTAL_SCORE"]["total_score"] += 1
        else:
            print("Wrong! Correct option is: ", q["answer"])
            progress[modules["title"]]["mistakes"] += 1
            progress["TOTAL_SCORE"]["total_mistakes"] += 1
        print()
    print(
        f"Score: {progress[modules['title']]['score']}, Mistakes: {progress[modules['title']]['mistakes']}"
    )
    print("")

# Summary of progress
total_questions = sum(len(m["quiz1"]) for m in lesson_data["modules"])
total_score = progress["TOTAL_SCORE"]["total_score"]
total_mistakes = progress["TOTAL_SCORE"]["total_mistakes"]
correct_answers = total_score / total_questions * 100

# printing summary
print("Progress Summary:\nTotal Questions: ", total_questions)
print("Overall Score: ", total_score)
print("Overall Mistakes: ", total_mistakes)
print("Total correct questions: ", correct_answers, "%")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")
