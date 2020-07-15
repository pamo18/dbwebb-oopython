#!/usr/bin/env python3
"""
Contains all classes for the different types of questions
"""
class Question():
    """Questions"""
    def __init__(self, answer, text):
        """Init"""
        self.type = "text"
        self.answer = answer
        self.text = text
        self.alternatives = []

    def get_type(self):
        """form type"""
        return self.type

    def get_text(self):
        """Question"""
        return self.text

    def get_alternatives(self):
        """Alernative answers"""
        return self.alternatives

    def check_answer(self, respons):
        """Check for points"""
        result = 0
        if self.answer == respons["answer"]:
            result += 1

        return result

class QuestionType2(Question):
    """Questions Type 2"""
    def __init__(self, answer, text, alt1, alt2, alt3):
        """Init"""
        super().__init__(answer, text)

        self.type = "checkbox"
        self.alternatives = [alt1, alt2, alt3]

    def check_answer(self, respons):
        """Check for multiple points"""
        result = 0
        for a in self.answer:
            if a in respons.getlist("answer"):
                result += 1

        return result

class QuestionType3(Question):
    """Questions Type 3"""
    def __init__(self, answer, text, alt1, alt2, alt3):
        """Init"""
        super().__init__(answer, text)

        self.type = "radiobutton"
        self.alternatives = [alt1, alt2, alt3]
