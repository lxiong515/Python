"""
Program: average_scores.py
Author: Luke Xiong
Last date modified: 6/6/2020

The purpose of this program is to take user input and read name,
age and test scores. Then average the test scores.
"""
import statistics
from statistics import mean

def average():
    # get user name
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    # get user age
    age = input("How old are you? ")
    # get input for scores
    score1 = int(input("Please enter test score #1: "))
    score2 = int(input("Please enter test score #2: "))
    score3 = int(input("Please enter test score #3: "))
    # created list of scores
    test_scores = [score1, score2, score3]
    # calculated average by importing statistics
    average_scores = (statistics.mean(test_scores))
    # return the user input and average test score
    return last_name + ", " + first_name + " age: " + age + " grade: " + str(average_scores)

print(average())
