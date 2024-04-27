def rationalization(number: float) -> str:
    """
    функция для приведения десятичной дроби в рациональный вид.
    """
    orders: list[int] = [1, 10, 100, 1000, 10000]
    numerator: int = 0
    denominator: int = 0
    for order in orders:
        if str(number * order)[-2] == "." and str(number * order)[-1] == "0":
            numerator = int(number * order)
            denominator = order
            break
    for i in range(1, 10):
        if numerator % i == 0 and denominator % i == 0:
            numerator //= i
            denominator //= i
    if denominator == 0:
        raise ArithmeticError()
    return f"{numerator} / {denominator}"


if __name__ == "__main__":
    print(rationalization(1.2))
