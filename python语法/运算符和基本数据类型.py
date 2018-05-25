"""

1.运算符
    结果是值
        算数运算
            a = 10 * 10
        赋值运算
            a = a + 1   a += 1
    结果是布尔值
        比较运算
            a = 1 > 5
        逻辑运算
            a = 1 >6 or 1 == 1   # 注意短路原则
        成员运算
            a = 1 in range(2)

2.基本数据类型
    整型   int  
        python3中   一切整型都是int
        python2中   短的叫int, 足够长叫long
    字符串  str
    布尔值  bool
    
"""

# 整型的魔法  
a = '10'
print(type(a), a)
b = int(a)             # 默认转换成10进制
print(type(b), b)
c = int(a, base=16)    # 转换成16进制
print(type(c), c)

age = 10
r = age.bit_length()
print(r)


# 字符串的魔法
test = "Yaya"
# 所有变小写
v1 = test.casefold()    #更牛逼
print(v1)
v2 = test.lower()   # 只适合英文，更常用
print(v2)
# 设置宽度并将内容居中，20指总宽度，*表示空白处填的字符
v3 = test.center(20, '*')   
print(v3)
# 计算当前字符串中有几个该字母
v4 = test.count('a')
print(v4)