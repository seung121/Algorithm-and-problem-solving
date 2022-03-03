import main


def SelectionSort(l):       # 선택정렬
    for i in range(len(l) - 1):
        min = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min]:
                min = j
        l[i], l[min] = l[min], l[i]
    return l

list = SelectionSort(main.RandomData)

print(" [:10] :", list[:10], "\n 가독성을 위한 생략\n", "[-10:] : ", list[-10:])

main.check(list)