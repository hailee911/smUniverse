import datetime

# 현재년도 2024
b = datetime.datetime.now().year

a = input ('생일 입력>> ')

print(f'현재나이 :{b - int(a[:4])}')

