class A:
    def __new__(cls, unit, qty):
        # def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.unit = unit
        instance.qty = qty
        return instance


a1 = A("Plane", 3000)
print(a1.unit, a1.qty)


class B:
    TOTAL_OBJ = 0

    def __init__(self) -> None:
        B.TOTAL_OBJ += 1

    @classmethod
    def func(cls, *args, **kwargs):
        return f"Total objects - {cls.TOTAL_OBJ}"


b1 = B()
b2 = B()
b3 = B()

print(B.func())  # 3
