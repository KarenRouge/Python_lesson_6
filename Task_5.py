class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'



class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} пишет.'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} делает набросок.'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} выделяет главное.'


red_pen = Pen("Ручка")
print(red_pen.draw())
grey_pencil = Pencil("Карандаш")
print(grey_pencil.draw())
yellow_handle = Handle("Маркер")
print(yellow_handle.draw())
