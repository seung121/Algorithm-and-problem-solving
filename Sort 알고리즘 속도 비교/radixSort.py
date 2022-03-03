import main

def getrdx(l, modulus):
    maxi = 0
    for val in l:
        digit = 0
        while val > 0:
            digit += 1
            val //= modulus
        if (digit > maxi):
            maxi = digit
    return(maxi)


def radixSort(l):
    radix, modulus, div = 10, 10, 1
    nordx = getrdx(l, modulus)
    for i in range(nordx):
        buckets = [[] for i in range(radix)]
        for value in l:
            buckets[(value % modulus) // div].append(value)
        modulus, div = modulus * 10, div * 10
        l = []
        for x in buckets:
            l.extend(x)
    return(l)

list = radixSort(main.RandomData)

print(" [:10] :", list[:10], "\n 가독성을 위한 생략\n", "[-10:] : ", list[-10:])

main.check(list)