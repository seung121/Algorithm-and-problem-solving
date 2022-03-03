import main

def InsertSort(l):
    for i in range (1, len(l)):
        CurrentElement = l[i]
        j = i - 1

        while (j >= 0) and l[j] > CurrentElement:
            l[j+1] = l[j]
            j = j - 1
        l[j + 1] = CurrentElement
    return l

list = InsertSort(main.RandomData)

print(" [:10] :", list[:10], "\n 가독성을 위한 생략\n", "[-10:] : ", list[-10:])

main.check(list)