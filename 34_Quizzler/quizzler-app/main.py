from data import get_data
from quiz_brain import QuizBrain
from question_model import Question
from ui import QuizInterface


question_list = []

question_data = get_data()

for question in question_data:
    question_text = question["question"]
    q_answer = question["correct_answer"]
    q = Question(question_text, q_answer)
    question_list.append(q)

quiz = QuizBrain(question_list)
quiz_ui = QuizInterface(quiz_brain=quiz)


# while quiz.still_has_questions():
#     quiz.next_question()

print("You've Completed Quiz")
# print(f"Your score is {quiz.score}/{quiz.question_number}")

