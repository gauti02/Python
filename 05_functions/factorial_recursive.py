def factorial_recursive(n: int) -> int:
    factorial = 1
    while n!=1:
        factorial *= n
        n -= 1
    return factorial
print(factorial_recursive(5))