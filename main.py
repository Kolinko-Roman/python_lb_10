def factorial_recursive(n):
    if not isinstance(n, int):
        raise ValueError("Аргумент має бути цілим числом.")
    if n < 0:
        raise ValueError("Факторіал не визначений для від'ємних чисел.")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    if not isinstance(n, int):
        raise ValueError("Аргумент має бути цілим числом.")
    if n < 0:
        raise ValueError("Число Фібоначчі не визначене для від'ємних чисел.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def sum_list_recursive(lst):
    if not isinstance(lst, list):
        raise ValueError("Аргумент має бути списком.")
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])


def is_palindrome_recursive(s):
    if not isinstance(s, str):
        raise ValueError("Аргумент має бути рядком.")
    
    s = ''.join(c.lower() for c in s if c.isalnum())

    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

# Тестування factorial_recursive
assert factorial_recursive(0) == 1
assert factorial_recursive(1) == 1
assert factorial_recursive(5) == 120
assert factorial_recursive(7) == 5040

# Тестування fibonacci_recursive
assert fibonacci_recursive(0) == 0
assert fibonacci_recursive(1) == 1
assert fibonacci_recursive(5) == 5
assert fibonacci_recursive(7) == 13

# Тестування sum_list_recursive
assert sum_list_recursive([]) == 0
assert sum_list_recursive([1]) == 1
assert sum_list_recursive([1, 2, 3, 4, 5]) == 15
assert sum_list_recursive([-1, 1, -2, 2]) == 0

# Тестування is_palindrome_recursive
assert is_palindrome_recursive("") is True
assert is_palindrome_recursive("a") is True
assert is_palindrome_recursive("racecar") is True
assert is_palindrome_recursive("A man a plan a canal Panama") is True
assert is_palindrome_recursive("hello") is False

print("Усі тести пройдено успішно!")
