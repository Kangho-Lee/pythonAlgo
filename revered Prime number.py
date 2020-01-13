import sys
# sys.stdin = open("input.txt", mode = "rt")

def reverse(x):
    res = 0
    while x != 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x):
    if x == 1 : return False
    for i in range(2,x):
        if round(x%i) == 0:
            # print(round(x%i))
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

output = list()

for i in range(n):
    reversed = reverse(a[i])
    if(isPrime(reversed)):
        output.append(reversed)

for j in range(len(output)):
    print(output[j], end=' ')
