def insertion_sort(numbers):
    print(f"before {numbers}")
    n = len(numbers)
    if n <= 1:
        return
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
