#!/usr/bin/env python3
"""
Contains the handler/manager class for the questions.
"""
from questions import Question
from questions import QuestionType2
from questions import QuestionType3

class QuestionManager():
    """Question handler"""
    def __init__(self):
        """Init"""
        self.questions = []
        self.score = 0
        self.quest_count = 0
        self.max_score = 12
        self.max_quest = 9
        self.make_questions()

    def make_questions(self):
        """Make the questions"""
        q1 = Question("Manchester", "What city do i originate from? \
        (Capital letter first)")
        q2 = Question("oopython", "What is this courses name? (small letters)")
        q3 = Question("Norway", "What country does Ole Gunnar Solskaer kommer \
        ifrån? (Capital letter first)")
        q4 = QuestionType2(["Orange", "Lemon"], "Which of the following fruits \
        are citrus?", "Apple", "Orange", "Lemon")
        q5 = QuestionType2(["Motor", "Wheels"], "Which of the following do you \
        normally find on a car?", "Cheese", "Motor", "Wheels")
        q6 = QuestionType2(["Hull", "Brighton"], "Which of the following are \
        British towns?", "Brighton", "Munich", "Hull")
        q7 = QuestionType3("-40", "What temperature is the same in Celsius and \
        Fahrenheit?", "-16", "+40", "-40")
        q8 = QuestionType3("Cuatro", "What number is next in the following \
        sequence? Uno, Dos, tres ?", "Cuatro", "Ocho", "Seis")
        q9 = QuestionType3("Britain", "What country might soon leave the \
        EU?", "Holland", "Britain", "Sweden")
        self.questions.append(q1)
        self.questions.append(q2)
        self.questions.append(q3)
        self.questions.append(q4)
        self.questions.append(q5)
        self.questions.append(q6)
        self.questions.append(q7)
        self.questions.append(q8)
        self.questions.append(q9)

    def get_score(self):
        """Score"""
        return self.score

    def get_max_score(self):
        """Max score"""
        return self.max_score

    def has_next(self):
        """Any questions left"""
        questions_left = bool(self.quest_count < self.max_quest)

        return questions_left

    def get_next(self):
        """Next question loads"""
        return self.questions[self.quest_count]

    def get_quest_count(self):
        """Current question"""
        return self.quest_count + 1

    def read_session(self, session):
        """Read session data"""
        if session.get("qstn"):
            self.quest_count = session.get("qstn")
            self.score = session.get("score")

    def write_session(self, session):
        """Write session data"""
        session["qstn"] = self.quest_count
        session["score"] = self.score

    def reset(self):
        """Reset stats"""
        self.score = 0
        self.quest_count = 0

    def correct_answer(self, form):
        """Correct answer or not"""
        result = self.questions[self.quest_count].check_answer(form)
        self.score += result
        self.quest_count += 1
