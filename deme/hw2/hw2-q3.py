#注：此题借助大模型
def calculate(s: str) -> int:
    def compute(num_stack, op_stack):
        b = num_stack.pop()
        a = num_stack.pop()
        op = op_stack.pop()
        if op == '+':
            num_stack.append(a + b)
        elif op == '-':
            num_stack.append(a - b)
        elif op == '*':
            num_stack.append(a * b)
        elif op == '/':
            num_stack.append(int(a / b))  # 注意Python除法向零取整

    num_stack = []
    op_stack = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    i = 0
    n = len(s)

    while i < n:
        if s[i] == ' ':
            i += 1
            continue
        if s[i].isdigit():
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            num_stack.append(num)
        elif s[i] == '(':
            op_stack.append(s[i])
            i += 1
        elif s[i] == ')':
            while op_stack[-1] != '(':
                compute(num_stack, op_stack)
            op_stack.pop()
            i += 1
        else:
            while op_stack and op_stack[-1] != '(' and priority[op_stack[-1]] >= priority[s[i]]:
                compute(num_stack, op_stack)
            op_stack.append(s[i])
            i += 1

    while op_stack:
        compute(num_stack, op_stack)

    return num_stack[0]


# e.g
print(calculate("3+5 * 8-6"))
print(calculate("34 + 13 * 9 + 44 - 12 / 3"))