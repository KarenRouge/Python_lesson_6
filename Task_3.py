class Worker:
    name = "Ivan"
    surname = "Ivanov"
    position = "Maneger"
    _income = {"Wage": 70000, "Bonus": 120000}


class Position(Worker):
    def get_full_name(self):
        self.name = Worker.name
        self.surname = Worker.surname
        ns = self.name + self.surname
        return ns

    def get_total_income(self):
        self.total_income = sum(Worker._income())
        return self.total_income

Worker.name = input("Введите имя сотрудника: ")
Worker.surname = input("Введите фамилию сотрудника: ")
Worker.position = input("Введите должность сотрудника: ")
a = input("Введите оклад сотрудника: ")
Worker._income["Wage"] = a
b = input("Введите премию сотрудника: ")
Worker._income["Bonus"] = b
print(Position.get_full_name(Worker.name, Worker.surname))
print(Position.get_total_income)
