class Car:
    speed = 50
    color = 'White'
    name = 'Honda'
    is_police = True

    def go(self, name):
        print(f'{name} goes!')

    def stop(self, name):
        print(f'{name} stop.')

    def turn(self, name, direction):
        print(f'{name} turned {direction}')

    def show_speed(self, name, speed):
        print(f"{name}' speed is {speed}")


class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        print(f'{color} {name} has {speed}.')
        if is_police is False:
            print("It's not a police!")

    def show_speed(self, name, speed):
        if speed < 60:
            print(f"{name}' speed is {speed} m/h.")
        else:
            print("Attention! Over speed!")


class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
        print(f'{color} {name} has {speed} m/h.')
        if is_police is False:
            print("It's not a police!")


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        print(f'{color} {name} has {speed} m/h.')
        if is_police is False:
            print("It's not a police!")

    def show_speed(self, name, speed):
        if speed < 60:
            print(f"{name}' speed is {speed} m/h.")
        else:
            print("Attention! Over speed!")


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        print(f'{color} {name} has {speed} m/h.')
        if is_police is True:
            print("It's a police!")


honda = TownCar('Honda', 55, 'red', False)
print(honda.go('Honda'))
print(honda.show_speed('honda', 55))
ferrari = SportCar('Ferrari', 80, 'yellow', False)
print(ferrari.stop('Ferrari'))
print(ferrari.show_speed('Ferrari', 90))
chevrolet = WorkCar('Chevrolet', 45, 'grey', False)
print(chevrolet.turn('Chevrolet', "right"))
ford = PoliceCar('Ford', 30, 'black', True)
print(ford.go("Ford"))
