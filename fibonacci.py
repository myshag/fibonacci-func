def fibonacci(n):
    """Возвращает первые n чисел Фибоначчи"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])
    return result


if __name__ == "__main__":
    # Выводим первые 15 чисел Фибоначчи
    fib_numbers = fibonacci(15)
    print(f"Первые 15 чисел Фибоначчи: {fib_numbers}")
    print(f"Сумма: {sum(fib_numbers)}")
