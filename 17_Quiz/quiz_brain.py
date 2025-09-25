class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def check_answer(self,answer, user_answer):
        if answer.lower() == user_answer.lower():
            print("Correct Answer!")
            self.score += 1
        else:
            print("Wrong Answer!")
            print("Correct Answer is:", answer)
    
        print("Score is:",self.score)

    def next_question(self):
        question_text = self.questions_list[self.question_number].text
        answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        question = f"Q.{self.question_number}: {question_text} (True/False)?:"
        user_answer = input(question)
        self.check_answer(answer, user_answer)
        