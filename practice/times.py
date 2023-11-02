import datetime


t = datetime.datetime.now()
current_day = t.strftime("%A")


td = datetime.timedelta(days=1)

start = datetime.datetime(2023, 10, 1)

for i in range(20):
    res = start + td
    print(res)
    start = res
