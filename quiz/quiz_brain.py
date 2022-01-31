class QuizBrain:

    def __init__(self, data):
        self.question_number = 0
        self.question_list = data
        self.score = 0

    def next_question(self):
        """Ask question, check answer and switch to another question"""
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1} {question.text} (True/False)?: ")
        self.check_answer(user_answer.lower(), question.answer.lower())
        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")
        self.question_number += 1

    def got_questions(self):
        """Return True if quiz have more questions, False otherwise"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, answer):
        """Check if user and right answers are equal. Increase score"""
        if user_answer == answer:
            print("You got it RIGHT")
            self.score += 1
        else:
            print("You got it WRONG")


