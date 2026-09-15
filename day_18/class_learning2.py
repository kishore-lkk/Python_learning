class car:
    wheels = 4
    def __init__(self, milage, company, cost):
        self.milage = milage
        self.company = company
        self.cost = cost

    @classmethod
    def wheel(cls):
        return cls.wheels

    @staticmethod
    def info():
        print("thi is car ordering system")


car1 = car(10, "bmw", 100)
car2 = car(12,"tesla", 200)

print(car.info())
