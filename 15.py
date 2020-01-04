#to build a basic calculator using if-else
def calc(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == '%':
        return num1 % num2


num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))
result = calc(num1, num2, op)
print(result)
