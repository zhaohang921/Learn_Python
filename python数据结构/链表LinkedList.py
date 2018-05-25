# 链表的实现
class LinkedList:

    class __Node:
        def __init__(self, item, next = None):
            self.item = item
            self.next = next

        def get_item(self):
            return self.item
        
        def set_item(self, item):
            self.item = item

        def get_next(self):
            return self.next

        def set_next(self, next):
            self.next = next

    def __init__(self, contents = []):
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.num_items = 0      # 元素数量
        for i, e in enumerate(contents):
            if i == 1:
                self.first = self.first.get_next()
            self.append(e)
    
    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.set_next(node)
        self.last = node
        self.num_items += 1

    # 可以用下标取值
    def __getitem__(self, index):
        if index >= 0 and index < self.num_items:
            cursor = self.first
            for i in range(index):
                cursor = cursor.get_next()
            return cursor.get_item()
        raise IndexError("LinkedList index out of range")

    # 可以用下标赋值
    def __setitem__(self, index, val):
        if index >= 0 and index < self.num_items:
            cursor = self.first
            for i in range(index):
                cursor = cursor.get_next()
            cursor.set_item(val)
            return
        raise IndexError("LinkedList assignment index out of range")

    # 重载+, 拼接两条链表
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + str(type(self)) + " + " + str(type(other)))
        result = LinkedList()
        cursor = self.first
        while cursor != None:
            result.append(cursor.get_item())
            cursor = cursor.get_next()
        cursor = other.first.get_next()
        while cursor != None:
            result.append(cursor.get_item())
            cursor = cursor.get_next()
        return result

    def insert(self, index, item):
        cursor = self.first
        if index < self.num_items:
            for i in range(index):
                cursor = cursor.get_next()
            node = LinkedList.__Node(item, cursor.get_next())
            cursor.set_next(node)
            self.num_items += 1
        else:
            self.append(item)

linkedList1 = LinkedList([1, 2, 3, 4, 5])
linkedList2 = LinkedList([9, 8, 7, 6])
print(linkedList1.first.item)
print(linkedList1[2])
linkedList1.append('append')
linkedList1.insert(2, 'insert')
linkedList1 += linkedList2
for i in linkedList1:
    print(i)    