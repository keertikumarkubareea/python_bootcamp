"""
The quiz brain class is responsible to
* Ask the questions
* Check if the answer was correct
* Check if we're at the end of the quiz
"""


class QuizBrain:
    def __init__(self, question_list: list):
        self.question_number = 0
        self.question_list = question_list

    def get_question(self):
        # Grab the current question and move the question number by 1
        question = self.question_list[self.question_number]
        self.question_number += 1
        return question

    def ask_next_question(self) -> str:
        if self.question_number >= len(self.question_list):
            return "completed"
        question = self.get_question()
        answer = input(f"Q.{self.question_number}: {question.question} (True/False): ").lower()
        while answer != "true" and answer != "false":
            answer = input("Please enter either True/False: ")
        return answer

    def validate_answer(self, answer: str) -> bool:
        return answer == self.question_list[self.question_number - 1].answer.lower()
