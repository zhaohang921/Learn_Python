# a = [66.25, 333, 333, 1, 1234.5]
# print(a.count(333), a.count(66.25), a.count('x'))


# 把列表当作堆栈使用
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)


# 列表推导式
squares = [x**2 for x in range(10)]
print(squares)
a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(a)