import re
expr = input()
operators = re.sub(r'\d', '', expr)
operands = list(map(int, re.split(r'[+,-]', expr)))
i = operators.find('-') + 1
print(sum(operands[:i]) - sum(operands[i:]) if i else sum(operands))