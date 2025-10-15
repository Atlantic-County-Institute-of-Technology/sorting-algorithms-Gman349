import time


def bubble_sort(numbers):
    lc = 0
    sc = 0
    start_time = time.time()
    print(f"before {numbers}")
    for i in range(len(numbers) - 1):
        lc = lc+1
        for j in range(len(numbers) - i - 1):
            lc = lc + 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                sc = sc + 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"after {numbers}")
    print(f"Loop count: {lc}")
    print(f"Sorting actions: {sc}")
    print(f"Time elapsed: {elapsed_time:.2f}s")
