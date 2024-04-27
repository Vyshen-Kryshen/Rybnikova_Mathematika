from schyot import *


def circle_area(radius: int) -> int:
    """
    функция расчёт площади круга.
    """
    result: int = int(summation(PI, radius))
    return result


def cylinder_volume(radius: int, height: int) -> int:
    """
    функция расчёта объёма цилиндра.
    """
    result: int = int(summation(PI, radius ** 2, height))
    return result


def ball_volume(radius: int) -> int:
    """
    функция расчёта объёма шара.
    """
    result: int = int(summation(2 / 3, cylinder_volume(radius, radius)))
    return result


if __name__ == "__main__":
    print(circle_area(5))
    print(cylinder_volume(10, 6))
    print(ball_volume(5))
