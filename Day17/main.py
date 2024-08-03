from question_model import Question
from data import question_data
import data
from quiz_brain import QuizBrain

"""
For new questions API: https://opentdb.com/api_config.php, reformat JSON response into a list of dictionaries
"""


def main():
    question_bank = []
    # Creating the question bank of Question objects
    for item in question_data:
        # Creating the Question object
        question = Question(question=item[data.TEXT], answer=item[data.ANSWER])
        # Appending the question object to the question_bank list
        question_bank.append(question)
    quiz_brain = QuizBrain(question_list=question_bank)
    completed = False
    count_correct = 0
    while not completed:
        user_answer = quiz_brain.ask_next_question()
        if user_answer == "completed":
            print(f"Congratulations! You have won with a score of {count_correct}.")
            completed = True
        else:
            if not quiz_brain.validate_answer(answer=user_answer):
                print(f"Wrong! Your score is {count_correct}.")
                completed = True
            else:
                count_correct += 1
                print(f"Correct. Your score is {count_correct}")
    print("Guessing game over")


if __name__ == "__main__":
    main()
