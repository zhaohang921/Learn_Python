
# 栈的实现，基于列表
class Stack:
    def __init__(self, *args):
        self._stack = []
        for i in args:
            self._stack.append(i)
        
    def size(self):
        return len(self._stack)

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        if self.size() > 0:
            return self._stack.pop()
        else:
            print("Sorry, this is an empty stack")

    def top(self):
        if self.size() > 0:
            return self._stack[len(self._stack) - 1]
        else :
            return "empty satck"


# 检查括号是否匹配
while True:
    stack = Stack()
    str = input('input the arithmetic expression:')
    if len(str) == 0:
        print("input something")
    else:
        for i in str:
            if i in '({[':
                stack.push(i)
            elif i in ')}]':
                stack.pop()
        if stack.size() == 0:
            print('It is a balanced arithmetic expression')
        else:
            print('not a balanced arithmatic expression')

