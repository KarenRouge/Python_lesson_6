class TrafficLight:
    color = "red"

    def running(self):
        print(self)
        import time
        time.sleep(7)
        _color = "yellow"
        print(self)
        time.sleep(2)
        _color = "green"
        print(self)
        time.sleep(3)
        print("Stop")
        return


example = TrafficLight
print(example.color)
