import main

def ShellSort(l):
    h = [701, 301, 132, 57, 23, 10, 4, 1]
    for g in range (len(h)):
        for i in range(h[g], len(l)):
            CurrentElement = l[i]
            j = i
            while j >= h[g] and l[j-h[g]] > CurrentElement:
                l[j] = l[j-h[g]]
                j = j-h[g]
            l[j] = CurrentElement
    return l

list = ShellSort(main.RandomData)

print(" [:10] :", list[:10], "\n 가독성을 위한 생략\n", "[-10:] : ", list[-10:])

main.check(list)