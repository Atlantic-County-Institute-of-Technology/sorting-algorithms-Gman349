import time


def bubble_sort(numbers):
    # variables
    num_before = str(numbers)
    lc = 0
    sc = 0
    start_time = time.time()  # get time
    for i in range(len(numbers) - 1):
        lc = lc + 1
        for j in range(len(numbers) - i - 1):  # run for every item in loop
            lc = lc + 1
            if numbers[j] > numbers[j + 1]:  # if a is larger then b, swap them
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                sc = sc + 1
    end_time = time.time()  # get time
    elapsed_time = end_time - start_time  # difference of times
    print(f"before {num_before}")
    print(f"after {numbers}")
    print(f"Loop count: {lc}")
    print(f"Sorting actions: {sc}")
    print(f"Time elapsed: {elapsed_time:.2f}s")
