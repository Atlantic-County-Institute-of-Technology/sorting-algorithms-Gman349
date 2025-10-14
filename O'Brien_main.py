import random
import inquirer3
from inquirer3.themes import *
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import *


def qstns(num1):
    minm = get_integer_input("Minimum random number:")
    maxm = get_integer_input("Maximum random number:")
    r_num = get_integer_input2("How many numbers in the list?")
    num1 = str([random.randint(minm, maxm) for i in range(r_num)])
    return num1


num = ""


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a number 0 or above")
                continue
            return value
        except ValueError:
            print("Please enter a number.")


def get_integer_input2(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Please enter a number 1 or above")
                continue
            return value
        except ValueError:
            print("Please enter a number.")


def main():
    while True:

        questions = [
            inquirer3.List('menu',
                           message="What would you like to do?",
                           choices=['Exit', 'Use Bubble sort', 'Use Insertion sort', 'Use selection sort'],
                           ),
        ]
        answers = inquirer3.prompt(questions)
        selct = "{}".format(answers['menu'])
        match selct:
            case "Exit":
                exit()
            case "Use Bubble sort":
                qstns(num)
                bubble_sort(num)
                print(f"after {num}")
            case "Use Insertion sort":
                qstns(num)
                insertion_sort(num)
                print(f"after {num}")
            # case "Use selection sort":


if __name__ == "__main__":
    main()
