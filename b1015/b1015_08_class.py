# from SS import *
# from math import
# SS모듈 함수 호출
# import math as ma
# stu_output()

# print(ma.floor(1.23))
# print(ma.ceil(1.23))
# print(ma.round(1.56))

from urllib import request

target = request.urlopen("http://www.google.com")
output = target.read()
print(output)