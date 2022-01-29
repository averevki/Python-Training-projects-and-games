#!/usr/bin/env python3

# Aleksandr Verevkin
# Quiz project with Object-Oriented Programing style

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

if __name__ == "__main__":
    question_data = [Question(question["text"], question["answer"]) for question in question_data]

    quiz = QuizBrain(question_data)

    while quiz.got_questions():
        quiz.next_question()

    print("Your final score is {}/{}".format(quiz.score, quiz.question_number))
    print("Thanks for playing")
