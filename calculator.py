a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = input("Введите действие: ")
if c == "/" and b == 0:
    print("На ноль делить нельзя")
elif c == "/":
    print(a / b)
elif c == "*":
    print(a * b)
elif c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "**":
    print(a ** b)
else:
    print("Некорректная операция ")