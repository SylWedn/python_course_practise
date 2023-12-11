
num1 = float(input("num1: "))
num2 = float(input("num2: "))
op = input("chose + - * / : ")

if op == "+":
    res = num1+num2
    print(res)
elif op =="-":
    res = num1-num2
    print(res)
elif op =="*":
    res = num1*num2
    print(res)
elif op =="/":
    res = num1/num2
    print(res)
else:
    print("USE NUMBERS AND + - * / OOKKK???!!")
