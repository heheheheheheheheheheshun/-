def planet(A):
    stack = []
    for planet in A:
        while stack and planet < 0 < stack[-1]:
            if abs(planet) > abs(stack[-1]):
                stack.pop()
                continue
            break
        else:
            stack.append(planet)
    return stack

# e.g
A1 = [-3, -6, 2, 8, 5, -8, 9, -2, 1]
result1 = planet(A1)
print(result1)
A2=[23,-8, 9, -3, -7, 9, -23, 22]
result2 = planet(A2)
print(result2)

