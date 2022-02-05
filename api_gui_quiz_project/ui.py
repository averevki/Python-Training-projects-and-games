from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInter:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.quit_but = None

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.l_score = Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.l_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, text="Question", width=280, fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=35)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_but = Button(image=self.true_img, highlightthickness=0, command=self.answer_true)
        self.true_but.grid(column=0, row=2)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_but = Button(image=self.false_img, highlightthickness=0, command=self.answer_false)
        self.false_but.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.true_but.config(state="normal")
            self.false_but.config(state="normal")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"Final score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_but.config(state="disabled")
            self.false_but.config(state="disabled")
            self.quit_but = Button(text="Quit", highlightthickness=0, command=self.window.destroy)
            self.quit_but.grid(column=0, row=0)

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("true"))
        self.renew_score()

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("false"))
        self.renew_score()

    def renew_score(self):
        self.l_score.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, answer: bool):
        self.true_but.config(state="disabled")
        self.false_but.config(state="disabled")
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
