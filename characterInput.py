'''
Author:         Justin Soderstrom
Date:           5/22/2016
Description:    My solution to Practice Python Character Input problem. Includes extras.
                http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
'''
from datetime import date

def solution(name, age, copys):
    year = date.today().year + (100 - age)
    for i in range(copys):
        print(name + ", you will turn 100 in the year " + str(year))
     

if __name__ == "__main__":
    name = input("What is your name? ")
    age = int(input("Hello " + name + ". How old are you? "))
    copys = int(input("How many messages should I print to the screen? "))
    solution(name, age, copys)
