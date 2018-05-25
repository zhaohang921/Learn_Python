
def quick_sort(array, lhs, rhs):
    if lhs < rhs:
        q = partition(array, lhs, rhs)
        quick_sort(array, lhs, q-1)
        quick_sort(array, q + 1, rhs)

def partition(array, lhs, rhs):
    x = array[rhs]          # 最右边的数是基准数
    i = lhs - 1 
    for j in range(lhs, rhs):   # 比基准数小的放在左边，比基准数大的放在右边
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[rhs] = array[rhs], array[i + 1]   # 把基准数放在中间位置
    return i + 1    # 返回基准数当前的位置



test = [1, 342, 4, 45, 64, 6, 4, 6, 7, 3, 55, 555, 5555, 343]

print(test)

quick_sort(test, 0, len(test) - 1)

print(test)
