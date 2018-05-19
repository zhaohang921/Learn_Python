# 道生一：传入type
class SayMetaClass(type):

    # 传入三大永恒命题：类名称、父类、属性
    def __new__(cls, name, bases, attrs):
        # 创造“天赋”
        attrs['say_'+name] = lambda self,value,saying=name: print(saying+','+value+'!')
        # 传承三大永恒命题：类名称、父类、属性
        return type.__new__(cls, name, bases, attrs)

# 一生二：创建类
class Hello(object, metaclass=SayMetaClass):
    pass

# 二生三：创建实例
hello = Hello()

# 三生万物：调用实例方法
hello.say_Hello('world')

# 一生二：创建类
class Sayolala(object, metaclass=SayMetaClass):
    pass

# 二生三：创建实例
s = Sayolala()

# 三生万物：调用实例方法
s.say_Sayolala('japan')

# 一生二：创建类
class Nihao(object, metaclass=SayMetaClass):
    pass

# 二生三：创建实例
n = Nihao()

# 三生万物：调用实例方法
n.say_Nihao('China')


