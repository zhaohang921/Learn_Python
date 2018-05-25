# 队列的实现，基于列表
class Queue:
    def __init__(self, *args):
        self._queue = []
        for i in args:
            self._queue.insert(0, i)  # 列表右边是队头

    def size(self):
        return len(self._queue)

    def is_empty(self):
        if self.size() == 0:
            return True
    
    def enqueue(self, *args):    # 入队
        for i in args:
            self._queue.insert(0, i)
    
    def dequeue(self):      # 出队
        if self.size() > 0:
            return self._queue.pop()
        else:
            print("empty queue")


# 约瑟夫环，用循环队列解决
names = input('plz input the names(with blank betwwwn them):')
judge = int(input('plz input the judge number:'))
flag = 1
queue = Queue()
for i in names.split(" "):
    queue.enqueue(i)
while queue.size() != 1:
    if flag != judge:
        queue.enqueue(queue.dequeue())
        flag += 1
    else:
        queue.dequeue()
        flag = 1
# 求出最后剩下的人
print(queue._queue)

    
    
