
# def adjust(li, i):
#     '''
#         调整结点
#     '''
#     l, r = i * 2 + 1, i * 2 + 2
#     while r < len(li) or l < len(li):
#         if r < len(li): # 有2个子结点
#             if max(li[l], li[r]) > li[i]:
#                 if li[l] > li[r]:
#                     li[i], li[l] = li[l], li[i]
#                     i = l
#                 else:
#                     li[i], li[r] = li[r], li[i]
#                     i = r
#             else:
#                 return
#         elif l < len(li): # 有1个结点
#             if li[l] > li[i]:
#                 li[i], li[l] = li[l], li[i]
#                 i = l
#             else:
#                 return
#         l, r = i * 2 + 1, i * 2 + 2


# def stack_sort(li, reverse=False):
#     if len(li) <= 1:
#         return

#     i = len(li)-1

#     while i > 0:
#         k = (i-2)//2 if i % 2 == 0 else (i-1)//2 # 找到父索引
#         if li[i] > li[k]:
#             li[i], li[k] = li[k], li[i]
#         adjust(li, i)
#         i = k
#         adjust(li, i)
#     li[0], li[-1] = li[-1], li[0]
#     return stack_sort(li[:-1], reverse)

# ###
def adjust(li, i, length):
    tmp = li[i] # 当前位置的结点
    k = i * 2 + 1   # 指向左结点
    while k < length:
        if k+1 < length and li[k] < li[k+1]:    # < 改 > 逆序。若有右结点，且右结点更大，指向右结点
            k += 1
        if li[k] > tmp:     # > 改 < 逆序
            li[i] = li[k]
            # li[i], li[k] = li[k], li[i]   # 使用交换的话，可以去掉tmp有关的操作，但swap交换操作增多，其实只需要最后设置i为tmp即可
            i = k
        else:
            break

        k = i * 2 + 1
    li[i] = tmp


def stack_sort(li):
    # 1.构建最大/最小堆
    for i in range(len(li)//2 - 1, -1, -1): # 从第1个非叶子结点开始，从下到上，从右到左调整
        adjust(li, i, len(li))
    # 2.调整堆，交换堆顶和堆尾（当前i是尾部）
    for end in range(len(li)-1, 0, -1):
        li[0], li[end] = li[end], li[0]
        adjust(li, 0, end)


if __name__ == "__main__":
    # li = [5, 6, 3, 8, 2, 1, 7, 9]
    li = [4, 6, 8, 5, 9]
    # li = [9,8,7,6,5,4,3,2,1]
    # li = list(range(30, 0, -1))
    stack_sort(li)
    print(li)