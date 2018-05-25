# 双端队列的实现
class Deque:
    def __init__(self, *args):
        self._deque = []
        for i in args:
            self._deque.insert(0, i)    # 列表右边是队头

    def __len__(self):
        return len(self._deque)

    def size(self):
        return len(self._deque)

    def is_empty(self):
        return True if self.size() == 0 else False

    def add_front(self, *args):
        for i in args:
            self._deque.append(i)
    
    def add_rear(self, *args):
        for i in args:
            self._deque.insert(0, i)
        
    def remove_front(self):
        if self.size() > 0:
            self._deque.pop()
        else:
            print('empty deque, cannot dequeue anymore')

    def remove_rear(self):
        if self.size() > 0:
            self._deque.pop(0)
        else:
            print('empty deque, cannot dequeue anymore')


# 回文检验
flag = True
expression = input('plz input the string:')
deque = Deque()
for i in expression:
    deque.add_rear(i)
while deque.size() != 1 or 0:
    a = deque.remove_front()
    b = deque.remove_rear()
    if a != b:
        flag = False
        break
if flag:
    print('yes, it is huiwen')
else:
    print('nout a huiwen string')