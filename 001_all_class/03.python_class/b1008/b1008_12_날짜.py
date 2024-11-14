import datetime

today = datetime.datetime.today()

# 날짜 시간 밀리초
print(today)
now_date = today.strftime("%Y-%m-%d")
# 날짜 포맷
print(now_date)

now_datetime = today.strftime("%Y-%m-%d %H:%M:%S")

print(now_datetime)