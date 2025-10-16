import time


def selection_sort(numbers):
    num_before = str(numbers)
    lc = 0
    sc = 0
    start_time = time.time()
    n = len(numbers)
    for ind in range(n):
        lc = lc + 1
        min_index = ind

        for j in range(ind + 1, n):
            lc = lc + 1
            if numbers[j] < numbers[min_index]:
                min_index = j
                sc = sc + 1
        (numbers[ind], numbers[min_index]) = (numbers[min_index], numbers[ind])
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"before {num_before}")
    print(f"after {numbers}")
    print(f"Loop count: {lc}")
    print(f"Sorting actions: {sc}")
    print(f"Time elapsed: {elapsed_time:.2f}s")
