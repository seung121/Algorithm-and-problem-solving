import main

def BubbleSort(l):   # 버블정렬
    for p in range(0, len(l) - 1):
        for i in range(1, len(l)-p):
            if l[i - 1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
    return l

list = BubbleSort(main.RandomData)

print("[:10] :", list[:10], "\n 가독성을 위한 생략\n","[-10:] : ", list[-10:])

main.check(list)