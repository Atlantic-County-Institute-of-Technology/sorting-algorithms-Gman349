import random
import inquirer3
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort


def get_integer_input(prompt):  # checks if number is positive and an integer
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a number 0 or above")
                continue
            return value
        except ValueError:
            print("Please enter a number.")


def get_integer_input2(prompt):  # checks if number is above one and an integer
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

        questions = [  # menu code
            inquirer3.List('menu',
                           message="What would you like to do?",
                           choices=['Exit', 'Use Bubble sort', 'Use Insertion sort', 'Use selection sort'],
                           ),
        ]
        answers = inquirer3.prompt(questions)
        selct = "{}".format(answers['menu'])
        match selct:  # run code based off of menu answer
            case "Exit":
                exit()
            case "Use Bubble sort":  # gets user inputs and runs bubble sort
                minm = get_integer_input("Minimum random number:")
                maxm = get_integer_input("Maximum random number:")
                r_num = get_integer_input2("How many numbers in the list?")
                if minm <= maxm and r_num <= 18500:  # caps at around 20 seconds
                    if r_num > 10000:  # warning that it will take long
                        print("WARNING: MAY TAKE LONGER THAN 10 SECONDS")
                    num = [random.randint(minm, maxm) for i in range(r_num)]
                    bubble_sort(num)
                else:
                    if r_num > 18500:
                        print("Please use a smaller amount of numbers in the list")
                    else:
                        print("Please put the smallest number first")
            case "Use Insertion sort":  # gets user inputs and runs insertion sort
                minm = get_integer_input("Minimum random number:")
                maxm = get_integer_input("Maximum random number:")
                r_num = get_integer_input2("How many numbers in the list?")
                if minm <= maxm and r_num <= 34000:  # caps at around 20 seconds
                    if r_num > 20000:  # warning that it will take long
                        print("WARNING: MAY TAKE LONGER THAN 10 SECONDS")
                    num = [random.randint(minm, maxm) for i in range(r_num)]
                    insertion_sort(num)
                else:
                    if r_num > 34000:
                        print("Please use a smaller amount of numbers in the list")

                    else:
                        print("Please put the smallest number first")

            case "Use selection sort":   # gets user inputs and runs selection sort
                minm = get_integer_input("Minimum random number:")
                maxm = get_integer_input("Maximum random number:")
                r_num = get_integer_input2("How many numbers in the list?")
                if minm <= maxm and r_num <= 25000:  # caps at around 20 seconds
                    if r_num > 15000:  # warning that it will take long
                        print("WARNING: MAY TAKE LONGER THAN 10 SECONDS")
                    num = [random.randint(minm, maxm) for i in range(r_num)]
                    selection_sort(num)
                else:
                    if r_num > 25000:
                        print("Please use a smaller amount of numbers in the list")
                    else:
                        print("Please put the smallest number first")


if __name__ == "__main__":
    main()
