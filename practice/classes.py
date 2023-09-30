class Car:
    def __init__(self, brand):
        # При присвоении защищенной переменной, субкласс не может к ней обратиться.
        # self.__brand = brand
        self.brand = brand


class BMWCar(Car):
    instances = 0

    def __init__(self, brand: str, speed: int):
        super().__init__(brand)
        self.speed = speed

    def show_speed(self):
        return f"{self.brand}'s max speed is {self.speed} km/h."

    # Отобразится, если мы объект определяем на лету (в консоли Python)
    def __repr__(self) -> str:
        return f"{self.brand}"

    # Переписываем строчное представление объекта при принте
    def __str__(self) -> str:
        return f"Brand: {self.brand}, speed: {self.speed}"

    @classmethod
    def some_func(cls):
        cls.instances += 1
        return cls.instances


# bmw = BMWCar("BMW", 220)
# bmw_m = BMWCar("BMW M3", 235)


# Ensure only one instance of a class exists
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
