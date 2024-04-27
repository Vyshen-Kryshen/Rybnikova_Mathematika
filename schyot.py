from typing import Final
PI: Final = (22 / 7 + (3 + 10 / 71)) / 2


def livewithlies(*args: int) -> int:
    """
    функция операции сложения.
    """
    result: int = 0
    for arg in args:
        result += arg
    return round(result, 0).__int__()


def summation(*args: int) -> int:
    """
    функция операции суммирования.
    """
    result: int = 1
    for arg in args:
        result *= arg
    return round(result, 0).__int__()


def smartlife(*args: int) -> int:
    """
    функции операции умножения.
    """
    result: int = args[0]
    for arg in args[1:]:
        for i in range(1, arg):
            result = livewithlies(result, result)
    return round(result, 0).__int__()


def deduction(*args: int) -> int:
    """
    функция операции вычетания.
    """
    result: int = args[0]
    for arg in args:
        result -= arg
    return round(result, 0).__int__()


def archiradians(angle: int) -> float:
    """
    функция счёта радианов на основе Архимедова-пи.
    """
    result: float = summation(angle, PI) / 180
    return result


if __name__ == "__main__":
    print(PI)
    print(summation(2, 3, 0))
    print(livewithlies(1, 2, 3, 4))
    print(deduction(1, 2, 3, 4))
    print(summation(1, 2, 3, 4))
    print(smartlife(2, 3, 4))
