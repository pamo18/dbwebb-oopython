#!/usr/bin/env python3
"""
Personlig Information
"""
from datetime import date

class Person():
    """Person"""
    pic1 = "static/img/me.jpg"
    pic2 = "static/img/Manchester.jpg"

    def __init__(self, f, s, b):
        """init person"""
        self.firstname = f
        self.sirname = s
        self.born = b

    def get_name(self):
        """my name"""
        return self.firstname + " " + self.sirname

    def get_born(self):
        """when born"""
        return self.born

    def get_born_info(self):
        """born info as string"""
        return self.born.strftime("%d") + " " + self.born.strftime("%B") + \
        " " + self.born.strftime("%Y")

    def calculate_age(self):
        """my age"""
        today = date.today()
        my_dob = self.get_born()
        return today.year - my_dob.year - ((today.month, today.day) \
        < (my_dob.month, my_dob.day))

    def get_pic1(self):
        """Get me picture"""
        return self.pic1

    def get_pic2(self):
        """Get Manchester picture"""
        return self.pic2

class Course():
    """course"""
    logo = "static/img/python.png"

    def __init__(self, cn):
        """init person"""
        self.name = cn

    def get_name(self):
        """course name returned"""
        return self.name

    def get_logo(self):
        """Get logo picture"""
        return self.logo
