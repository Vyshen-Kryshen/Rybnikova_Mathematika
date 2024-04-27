from math import sin, cos, radians, atan2
from schyot import PI, livewithlies, deduction, summation, archiradians
import pygame


class Ninetyhexagon(pygame.surface.Surface):
    """
    Класс описывает 96-угольник, подобный кругу. Основывается на аспектах знаний Архимеда.
    В методах класса так же есть обращение к методу '__checker(self) -> None:', 
    для вызова исключений-ошибок связанных с атрибутом 'radius: int'.
    """
    __radius: int = 0
    location: tuple[int, int] = (0, 0)
    __angle: int = 0
    __points: list[tuple[int, int]] = []

    def __init__(self, radius: int, location: tuple[int, int], angle: int = 0) -> None:
        """
        По мимо создание динамического радиуса и расположения, мы так же кастим этот тип к батяному типу.
        """
        self.__radius = radius
        self.location = location
        self.__angle = angle
        self.__checker()
        super().__init__((radius, radius))

    def draw(self, surface: pygame.surface.Surface, color: str | tuple[int, int, int] | pygame.color.Color = "white", 
    archi: bool = True, trueadd: bool = True) -> None:
        """
        Метод отрисовки объекта, мы так же создаём и сортируем все точки данного многоугольника.
        """
        self.__checker()
        for i in range(0, 96):
            if archi:
                x: int = livewithlies(summation(self.__radius, cos(archiradians(self.__angle))), self.location[0])
                y: int = livewithlies(summation(self.__radius, sin(archiradians(self.__angle))), self.location[1])
            else:
                x: int = livewithlies(summation(self.__radius, cos(radians(self.__angle))), self.location[0])
                y: int = livewithlies(summation(self.__radius, sin(radians(self.__angle))), self.location[1])
            self.__points.append((x, y))
            if trueadd:
                self.__angle = livewithlies(self.__angle, 3.75)
            else:
                self.__angle += 3.75
        self.__points = sorted(self.__points, 
        key=lambda point: atan2(deduction(point[0], self.location[0]), 
        deduction(point[1], self.location[1])))
        pygame.draw.polygon(surface, color, self.__points, 0)
        self.__points.clear()

    def rotation(self, side: str = "right") -> None:
        """
        Этот метод реализует вращение Архимедова-круга.
        """
        self.__checker()
        if side == "right":
            self.__angle = livewithlies(self.__angle, PI)
        elif side == "left":
            self.__angle = livewithlies(self.__angle, -PI)
        else:
            raise ValueError(f"The side: {side} is not exist.")

    def __checker(self) -> None:
        if self.__radius < 1 or self.__radius > 10000:
            raise ValueError("Invalid radius value.")
        

if __name__ == "__main__":
    screen = pygame.display.set_mode((1200, 600))
    clock = pygame.time.Clock()
    c1 = Ninetyhexagon(100, (600, 300))
    while True:
        screen.fill("black")
        c1.draw(screen, "white", False, False)
        c1.rotation()
        c1.location = (c1.location[0] + 1, c1.location[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.flip()
        clock.tick(60)
