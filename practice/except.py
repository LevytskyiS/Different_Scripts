class MyCustomException(Exception):
    def __init__(self, message, extra_info):
        super().__init__(message)
        self.extra_info = extra_info


try:
    raise MyCustomException("Some error", {"code": 400, "time": "11:11"})
except MyCustomException as e:
    print(f"EXCEPTION: {e}")
    print(f"EXTRA INFO: {e.extra_info}")
