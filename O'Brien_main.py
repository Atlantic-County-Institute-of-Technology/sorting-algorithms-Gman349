import random
import inquirer3
from bubble_sort import bubble_sort
from insertion_sort import *
from selection_sort import *


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
                min = get_integer_input("minimum random number:")
                max = get_integer_input("maximum random number:")
                r_num = get_integer_input2("How many numbers in the list?")
                num = [random.randint(min, max) for i in range(r_num)]
                bubble_sort(num)
                print(f"after {num}")
            # case "Use Insertion sort":
            #
            # case "Use selection sort":


if __name__ == "__main__":
    main()
