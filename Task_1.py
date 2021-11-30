from time import sleep
class TrafficLight:
    _color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 3:
            print(TrafficLight._color[i])
            if i == 0:
                sleep(7)
            if i == 1:
                sleep(3)
            if i == 2:
                sleep(7)
            i = i + 1
        return

example = TrafficLight()
example.running()
