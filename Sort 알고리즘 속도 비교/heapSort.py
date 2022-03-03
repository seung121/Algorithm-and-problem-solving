import main
import heapq


def HeapSort(l):
    heap = []
    for num in l:
        heapq.heappush(heap, num)
    sorted_l = []
    while heap:
        sorted_l.append(heapq.heappop(heap))
    return sorted_l

list = HeapSort(main.RandomData)

print(" [:10] :", list[:10], "\n 가독성을 위한 생략\n", "[-10:] : ", list[-10:])

main.check(list)