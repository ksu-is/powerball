#!/usr/bin/env python

"""
If you happen to win, I only ask for a measly 1% tip. ;)
To run, save this file and run it by typing the following in your terminal:
python powerball.py
"""
from pprint import pprint as pp
import random

def powerball():
    drum1 = list(range(1,70))
    drum2 = list(range(1,27))
    white_balls = []
    
    for _ in range(5):
        choice = random.SystemRandom().choice(drum1)
        drum1.pop(drum1.index(choice))
        white_balls.append(choice)
    white_balls = sorted(white_balls)
    return white_balls + [random.SystemRandom().choice(drum2)]
    
try:
    budget = int(int(input('What is your powerball budget? (Number must be multiple of 2)'))/2)
except:
    budget = 1

pp(list(powerball() for i in range(budget)))
