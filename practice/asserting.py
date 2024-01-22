def some_func(a, b):
    return a + b


res = some_func(3, 2)
assert res == 5


class MyCustomException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            return self.balance
        try:
            raise MyCustomException("The amount of money is less or equal zero.")
        except MyCustomException as e:
            print(e)


ba1 = BankAccount(10)
assert ba1.balance == 10

ba1.deposit(-1)
assert ba1.balance == 14
