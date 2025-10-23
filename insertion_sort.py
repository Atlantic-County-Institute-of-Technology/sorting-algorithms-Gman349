import time


def insertion_sort(numbers):
    num_before = str(numbers)
    lc = 0
    sc = 0
    start_time = time.time()
    n = len(numbers)
    if n <= 1:
        return
    for i in range(1, n):
        lc = lc + 1
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            sc = sc + 1
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"before {num_before}")
    print(f"after {numbers}")
    print(f"Loop count: {lc}")
    print(f"Sorting actions: {sc}")
    print(f"Time elapsed: {elapsed_time:.2f}s")
