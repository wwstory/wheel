from random import randint

def quick_sort(li, start, end):
    # 0.退出条件
    if start >= end:
        return
    
    # 1.设置左/右/基准
    p = start   # p = randint(start, end)
    p = randint(start, end)
    l = start
    r = end

    # li[start], li[p] = li[p], li[start] # 交换基准到第1个

    # 2.双边循环交换
    while l < r:
        if li[r] > li[p]:
            r -= 1
            continue
        if li[l] <= li[p]:
            l += 1
            continue
        else:
            li[l], li[r] = li[r], li[l]

    # 3.交换后，放置基准到分割处
    li[p], li[l] = li[l], li[p] # 交换回来（此时，l在分割处）

    # 4. 分治
    p = l   # 找到中间分成2堆的位置
    quick_sort(li, start, p)
    quick_sort(li, p+1, end)


if __name__ == "__main__":
    li = [5, 6, 3, 8, 2, 1, 7, 9]
    quick_sort(li, 0, len(li)-1)
    print(li)