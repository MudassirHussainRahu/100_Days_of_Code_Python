from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

import os

def clear():
    os.system("cls")

question_bank = []

for q in question_data:
    question = Question(q["text"], q["answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
clear()
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

