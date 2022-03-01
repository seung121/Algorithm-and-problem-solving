def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = mergeSort(a[:mid])
    right = mergeSort(a[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:

            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]

            else:
                result.append(right[0])
                right = right[1:]

        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]

        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


alist = [4, 26, 9, 3, 1, 72, 566, 43]

mergeSort(alist)
blist = mergeSort(alist)

print(blist)
