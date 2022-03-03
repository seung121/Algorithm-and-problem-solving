import random

random.seed(100)

RandomData = []

for i in range(2000):
    RandomData.append(random.randint(0, 10000))

print(RandomData)

def check(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            print(l[i], l[i+1])
            print("잘못된 코드!")
            return
    print("오름차순 정렬이 올바르게 되어 있습니다.")

