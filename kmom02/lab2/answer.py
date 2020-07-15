#!/usr/bin/env python3

"""
cccb511499da632bb0f1463b2d30eaf5
oopython
lab2
v2
pamo18
2019-01-29 11:20:52
v3.1.3 (2018-09-13)

Generated 2019-01-29 12:20:52 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a *get* method for both "name" and "ssn". Only Create a *set* method
# for "name".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Skorstten` and ssn `541355-8072`.
#
#
# Answer with per\'s get method for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#
class Person():
    """person"""
    def __init__(self, name, ssn, address):
        """init"""
        self.name = name
        self.__ssn = ssn
        self.address = address

    def get_name(self):
        """name"""
        return self.name

    def get_ssn(self):
        """ssn"""
        return self.__ssn

    def set_name(self, new_name):
        """set name"""
        self.name = new_name

    def set_address(self, new_address):
        """address"""
        self.address = new_address

    def to_string(self):
        """to string"""
        return "Name: {name} SSN: {ssn} {adrs}".format(
            name=self.name,
            ssn=self.__ssn,
            adrs=self.address
        )

per = Person('Skorstten', '541355-8072', "")
result = per.get_ssn()




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
# Create a method, in Address, called **to_string**, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Add the instance attribute **address** to class Person. It's value should
# be sent as argument to constructor, give it a default value of and empty
# string, `""`.
# Create a set method for attribute "address".
# Create a method, in Person, called **to_string**, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"`. Use Address'
# to_string method to get address data.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Amador`, the state `Withywoods` and the country `Ademere`.
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#
class Address():
    """address"""
    def __init__(self, city, state, country):
        """init"""
        self.city = city
        self.state = state
        self.country = country

    def to_string(self):
        """to string"""
        return "Address: {city} {state} {country}".format(
            city=self.city,
            state=self.state,
            country=self.country
            )

first_address = Address('Amador', 'Withywoods', 'Ademere')

per.set_address(first_address.to_string())
result = per.to_string()



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person". In
# the constructor add the instance attribute "courses" and initiate it to and
# empty list.
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
# Create the method **remove_course**, it should take one argument and remove
# if from the course list attribute.
# Overload the **to_string** method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Tip, use `super(Teacher, self)` to access base
# method.
#
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Renere`, the state `Withywoods` and the country `Ceald`.
# Create a new instance of the class Teacher. Initiate it with the name
# `James` and ssn `503233-4011` and the aforementioned Address object.
# Use the add_course method to add the following courses, `webgl`, `ramverk2`
# and `oopython`.
#
#
# Answer with the Teacher object's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#
class Teacher(Person):
    """teacher"""
    def __init__(self, name, ssn, address):
        """init"""
        super().__init__(name, ssn, address)

        self.courses = []

    def add_course(self, course_to_add):
        """course add"""
        self.courses.append(course_to_add)

    def remove_course(self, course_to_remove):
        """course remove"""
        self.courses.remove(course_to_remove)

    def to_string(self):
        """to string"""
        return "{base_msg} Courses: {course_list}".format(
            base_msg=super().to_string(),
            course_list=", ".join(self.courses)
        )

second_address = Address('Renere', 'Withywoods', 'Ceald')
james = Teacher('James', '503233-4011', second_address.to_string())
james.add_course('webgl')
james.add_course('ramverk2')
james.add_course('oopython')

result = james.to_string()


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person". In
# the constructor add the instance attribute "courses_grades" and initiate it
# to and empty list.
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Imre`, the state `Norrland` and the country `Tear`.
# Create a new instance of the class Student. Initiate it with the name
# `Badgerlock` and ssn `768244-4857` and the aforementioned Address object.
# Use the add_course_grade method to add the following courses, `linux` with
# grade `0`, `ramverk1` with grade `-` and `oopython` with grade `2`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#
class Student(Person):
    """student"""
    def __init__(self, name, ssn, address):
        """init"""
        super().__init__(name, ssn, address)

        self.courses_grades = []

    def add_course_grade(self, course, grade):
        """grades"""
        course_result = (course, grade)
        self.courses_grades.append(course_result)

    def average_grade(self):
        """average grade"""
        count = 0
        grade_sum = 0
        for _x, _y in self.courses_grades:
            if _y != '-':
                count += 1
                grade_sum += int(_y)
        return grade_sum / count

third_address = Address('Imre', 'Norrland', 'Tear')

badgerlock = Student('Badgerlock', '768244-4857', third_address)
badgerlock.add_course_grade('linux', '0')
badgerlock.add_course_grade('ramverk1', "-")
badgerlock.add_course_grade('oopython', '2')

result = badgerlock.average_grade()



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)


dbwebb.exit_with_summary()
