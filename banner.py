'''
Author:       Justin Soderstrom
Date:         5/22/2016
Description:  Toy program to enter your name and create a variable sized banner around it.
'''
# ~/bin/python3

def banner(name):
    nameLength = len(name) + 4 #Plus 4 because of the two * (space)
    print('*' * nameLength, end="")
    print()
    print("* " + name + " *")
    print('*' * nameLength, end="")

if __name__ == "__main__":
    name = str(input("What's your name? "))
    banner(name)

