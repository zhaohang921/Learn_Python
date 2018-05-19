
# 定义：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）
def outer(x):
    # x = 10
    def inner():  # 条件一：inner就是内部函数
        print(x)  # 条件二：外部环境的一个变量
    
    return inner  # 内部函数inner就是一个闭包

# outer()()

f = outer(8)
f()

# 关于闭包：闭包=函数块+定义函数时的环境


import time 


# 功能函数加参数
def logger(flag=''):
    def show_time(func):
        def inner(*x, **y):
            start = time.time()
            func(*x, **y)
            end = time.time()
            print(end-start)
            if flag=='true':
                print('log...')
        return inner
    return show_time
    

# @show_time  # foo = show_time(foo)
# def foo():
#     print('foo...')
#     time.sleep(2)


# 装饰器加参数
@logger('true')  # @show_time 
def add(*a, **b):
    sums=0
    for i in a:
        sums += i
    print(sums)
    time.sleep(1)

add(1,2,3,4,5)


login_status = False

user = 'aaa'
pasd = 123

def login():
    if login_status == False:
        username = input("username:")
        password = input("password:")
        if user == username and pasd == password:
            print("Welcome...")
            login_status = True
        else:
            pass

