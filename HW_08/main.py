from Rational import Rational


def parse_expression(expr):
    tokens = expr.strip().split()
    if not tokens:
        return None

    def to_rational(token):
        if '/' in token:
            return Rational(token)
        else:
            return Rational(int(token), 1)

    values = []
    operators = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in "+-*/":
            operators.append(token)
        else:
            values.append(to_rational(token))
        i += 1

    i = 0
    while i < len(operators):
        op = operators[i]
        if op in '*/':
            a = values[i]
            b = values[i+1]
            if op == '*':
                res = a * b
            else:
                res = a / b
            values[i] = res
            del values[i+1]
            del operators[i]
        else:
            i += 1

    result = values[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += values[i+1]
        elif op == '-':
            result -= values[i+1]

    return result






with open("input01.txt", "r") as file:
    for line in file:
        try:
            res = parse_expression(line)
            print(f"Результат: {res} = {res():.3f}")
        except Exception as e:
            print(f"Помилка у рядку: {line.strip()} -> {e}")
