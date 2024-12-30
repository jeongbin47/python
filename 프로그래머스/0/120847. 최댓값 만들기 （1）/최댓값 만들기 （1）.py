def solution(numbers):
    n = max(numbers)
    n2 = numbers[0]
    if n == n2:
        n2 = numbers[1]
    for i in numbers:
        if n2 < i < n:
            n2 = i
    return n * n2