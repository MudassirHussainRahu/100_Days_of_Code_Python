import tkinter as tk
import time

from quiz_brain import QuizBrain
# from data import question_list


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):

        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = tk.Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, foreground="white")
        self.score.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.canvas.config(background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,width=280, text=f"{self.quiz.next_question()}",fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_img, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=0)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0,command=self.false_clicked)
        self.false_button.grid(row=2, column=1)
        
        self.window.mainloop()

    def true_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        # self.update()

    def false_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        # self.update()
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(2000, self.update)


    def update(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=f"{self.quiz.next_question()}")
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"Out of Questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            