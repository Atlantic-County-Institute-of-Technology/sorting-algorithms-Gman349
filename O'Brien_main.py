import random
import inquirer3
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort


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
                minm = get_integer_input("Minimum random number:")
                maxm = get_integer_input("Maximum random number:")
                r_num = get_integer_input2("How many numbers in the list?")
                if minm < maxm:
                    num = [random.randint(minm, maxm) for i in range(r_num)]
                    bubble_sort(num)
                else:
                    print("Please put the smallest number first")
            case "Use Insertion sort":
                minm = get_integer_input("Minimum random number:")
                maxm = get_integer_input("Maximum random number:")
                r_num = get_integer_input2("How many numbers in the list?")
                if minm < maxm:
                    num = [random.randint(minm, maxm) for i in range(r_num)]
                    insertion_sort(num)
                else:
                    print("Please put the smallest number first")
            case "Use selection sort":
                minm = get_integer_input("Minimum random number:")
                maxm = get_integer_input("Maximum random number:")
                r_num = get_integer_input2("How many numbers in the list?")
                if minm < maxm:
                    num = [random.randint(minm, maxm) for i in range(r_num)]
                    selection_sort(num)
                else:
                    print("Please put the smallest number first")


if __name__ == "__main__":
    main()
