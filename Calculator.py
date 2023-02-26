import math

def calculate(s):
    """
    Функция принимает строку арифметического выражения, возвращает результат вычисления
    """
    stack = []
    num = 0
    op = "+"
    s += "+0"  # добавляем операцию и 0 для завершения вычислений
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        elif not s[i].isspace():
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack[-1] *= num
            elif op == "/":
                stack[-1] = int(stack[-1] / float(num))
            elif op == "^":
                stack[-1] **= num
            elif op == "sqrt":
                stack[-1] = math.sqrt(stack[-1])
            elif op == "abs":
                stack[-1] = abs(stack[-1])
            elif op == "sin":
                stack[-1] = math.sin(stack[-1])
            elif op == "cos":
                stack[-1] = math.cos(stack[-1])
            elif op == "tan":
                stack[-1] = math.tan(stack[-1])
            num = 0
            op = ""
            while i < len(s) and not s[i].isdigit() and s[i] != ".":
                op += s[i]
                i += 1
            i -= 1
        i += 1
    return sum(stack)

print(calculate("2+2*5")) # Output: 12
print(calculate("2^3")) # Output: 8
print(calculate("sqrt 16")) # Output: 4.0
print(calculate("abs -4")) # Output: 4
print(calculate("sin 0")) # Output: 0.0
