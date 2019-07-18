


from pprint import pprint as pp
import random

def powerball():
    drum1 = list(range(1,70))
    drum2 = list(range(1,27))
    number_even = (random.randint(0,70)) * 2
    number_odd = (random.randint(0,70)) * 2 +1
    white_balls = []

    for _ in range(5):
        choice = random.SystemRandom().choice(drum1)
        drum1.pop(drum1.index(choice))
        white_balls.append(choice)
    white_balls = sorted(white_balls)
    return white_balls + [random.SystemRandom().choice(drum2)]
    
try:
    budget = int(int(input('How much money would you like to spend on tickets? (Each ticket cost $2)'))/2)
    
except:
    budget = 1

pp(list(powerball() for i in range(budget)))


