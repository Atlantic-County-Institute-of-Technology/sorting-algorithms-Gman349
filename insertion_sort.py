import time


def insertion_sort(numbers):
    # variables
    num_before = str(numbers)
    lc = 0
    sc = 0
    start_time = time.time()  # get time
    n = len(numbers)
    if n <= 1:
        return
    for i in range(1, n):  # run for every item in loop
        lc = lc + 1
        key = numbers[i]  # key = a
        j = i - 1
        while j >= 0 and key < numbers[j]:  # if b is more than key, move list over by one and insert key
            sc = sc + 1
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

    end_time = time.time()  # get time
    elapsed_time = end_time - start_time  # difference of times
    print(f"before {num_before}")
    print(f"after {numbers}")
    print(f"Loop count: {lc}")
    print(f"Sorting actions: {sc}")
    print(f"Time elapsed: {elapsed_time:.2f}s")
