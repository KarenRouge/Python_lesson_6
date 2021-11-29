class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        _income = {"Wage": wage, "Bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


employee = Position("Ivan", "Durak", "Royal groom", 10, 1500)

print(employee.get_full_name)
print(employee.position)
print(employee.get_total_income)
