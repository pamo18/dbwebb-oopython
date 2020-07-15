#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cat class"""

class Cat():
    """cat class"""
    lives_left = -1
    nr_of_paws = 4
    def __init__(self, eye_color, name):
        """cat init"""
        self.eye_color = eye_color
        self.name = name

    def get_eye_color(self):
        """get eyes"""
        return self.eye_color

    def get_name(self):
        """get name"""
        return self.name

    def get_lives_left(self):
        """get lives"""
        return self.lives_left

    def set_lives_left(self, lives):
        """set lives"""
        self.lives_left = lives
        return self.lives_left

    def get_nr_of_paws(self):
        """get paws"""
        return self.nr_of_paws

    def description(self):
        """description"""
        n = self.get_name()
        e = self.get_eye_color()
        l = self.get_lives_left()
        return "My cats name is " + n + ", has " + e + \
        " eyes and " + str(l) + " lives left to live."

class Duration():
    """Duration class"""
    def __init__(self, hours, minutes, seconds):
        """Duration init"""
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def info(self):
        """duration info h-m-s"""
        if self.hours < 10:
            h = "0" + str(self.hours)
        else:
            h = str(self.hours)

        if self.minutes < 10:
            m = "0" + str(self.minutes)
        else:
            m = str(self.minutes)

        if self.seconds < 10:
            s = "0" + str(self.seconds)
        else:
            s = str(self.seconds)

        return  h + "-" + m + "-" + s

    @staticmethod
    def duration_to_sec(s):
        """convert to seconds"""
        hour = (int(s[0:2]) * 60) * 60
        minutes = int(s[3:5]) * 60
        seconds = int(s[6:8])

        return hour + minutes + seconds

    def __add__(self, other):
        """add to other"""
        return self.duration_to_sec(self.info()) + \
        other.duration_to_sec(other.info())

    def __iadd__(self, other):
        """set self plus other"""
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds
        return self

    def __lt__(self, other):
        """if less than other"""
        return self.duration_to_sec(self.info()) < \
        other.duration_to_sec(other.info())
