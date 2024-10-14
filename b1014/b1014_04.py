# 함수 선언
def calc():
  if op == "+":
    return num+num2
  elif op == "-":
    return num-num2
  elif op == "*":
    return num*num2
  elif op == "/":
    return num/num2
  
num = int(input("숫자 입력 >> "))
num2 = int(input("숫자 입력 >> "))
op = input("+ - * / 하나를 선택하세요.")

print("결과값 : ",calc())

