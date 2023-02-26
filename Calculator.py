import math

def calculate(s):
    stack, num, op = [], 0, "+"
    s += "+0"
    for i, c in enumerate(s):
        if c.isdigit(): num = num * 10 + int(c)
        elif not c.isspace():
            if op == "+": stack.append(num)
            elif op == "-": stack.append(-num)
            elif op == "*": stack[-1] *= num
            elif op == "/": stack[-1] = int(stack[-1] / num)
            elif op == "^": stack[-1] **= num
            elif op == "sqrt": stack[-1] = math.sqrt(stack[-1])
            elif op == "abs": stack[-1] = abs(stack[-1])
            elif op == "sin": stack[-1] = math.sin(stack[-1])
            elif op == "cos": stack[-1] = math.cos(stack[-1])
            elif op == "tan": stack[-1] = math.tan(stack[-1])
            num, op = 0, c if c != "^" else "**"
            if c.isalpha(): op += " "
    return sum(stack)

print(calculate("2+2*5")) # Output: 12
print(calculate("2^3")) # Output: 8
print(calculate("sqrt 16")) # Output: 4.0
print(calculate("abs -4")) # Output: 4
print(calculate("sin 0")) # Output: 0.0
