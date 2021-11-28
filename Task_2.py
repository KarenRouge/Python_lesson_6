class Road:
    _length = 10
    _width = 5
    def road_weigth(self, length, width, sm_weigth, sm_width):
        self._length = length
        self._width = width
        sm_weigth = 25
        road_weigth = length * width * sm_weigth * sm_width
        return road_weigth

a = Road()
Road._length = int(input("Введите длину дороги в метрах: "))
Road._width = int(input("Введите длину дороги в метрах: "))
sm_width = int(input("Введите толщину асфальта: "))
print(f"Масса необходимого асфальта:{a.road_weigth(Road._length, Road._width, 25, sm_width)} тонн.")
