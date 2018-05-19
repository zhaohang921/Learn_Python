
pyList = [4, 12, 2, 34, 17]
print(pyList)

pyList.append(50)
print(pyList)
pyList.append(18)
print(pyList)
pyList.append(64)
print(pyList)
pyList.append(6)
print(pyList)

pyListA = [34, 12]
print(pyListA)
pyListB = [4, 6, 31, 9]
print(pyListB)
pyListA.extend(pyListB)
print(pyListA)
# 在第四个位置前插入79
pyList.insert(3, 79)
print(pyList)
pyList.pop(0)  # 移除第一个元素
print(pyList)
pyList.pop()   # 移除最后一个元素
print(pyList)

aSlice = pyList[2:4]
print(aSlice)

