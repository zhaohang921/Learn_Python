
# 列表生成式
def f(n):
    return n**3

a = [f(x) for x in range(10)] # 列表生成式
# print(a)
# print(type(a))

t=['123',8 ,23 ]
a, b, c = t
# print(a)
# print(b)
# print(c)


# 生成器
s = (x*2 for x in range(5))
print(s)

# print(next(s))  #等价于  s.__next__()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))  # StopIteration


# 生成器就是一个可迭代对象（Iterable）
for i in s:      # 垃圾回收机制
    print(i)

# 生成器一共两种生成方式
# s = (x*2 for x in range(5))
# yield

def foo():
    print('ok')
    yield 1
    print('ok2')
    yield 2

print(foo)
print(foo())

g=foo()
print(g)
print(next(g))
next(g)

# for i in foo():
#     print(i)


# 什么是可迭代对象（对象拥有__iter__方法）
l=[1,2,3]
l.__iter__()
t=(1,2,3)
t.__iter__()
d={'name':'123'}
d.__iter__()


# 斐波那契数列
def fib(max):
    n, before, after = 0, 0, 1
    while n < max:
        # print(after)
        yield before
        before , after = after, before + after
        n = n + 1

g=fib(8)
print(g)

print(next(g))

def bar():
    print('ok1')
    count = yield 1
    print(count)
    yield 2

b=bar()
# next(b)

b.send(None)  # 第一次send前如果没有next，只能传一个send(None)

b.send('eee')  # next(b)

# b.send('fff')


# yield 伪并发
import time 

def consumer(name):
    print("%s 准备吃包子啦" %name)
    while True:
        baozi = yield
        print("包子[%s]被[%s]吃了" %(baozi, name))

def producer(name):
    c = consumer('A')
    c1 = consumer('B')
    next(c)
    next(c1)
    print("zh开始准备做包子啦")
    for i in range(10):
        c.send(i)
        c1.send(i)
        time.sleep(1)

producer('zh')


# 迭代器
# 生成器其实是一种特殊的迭代器