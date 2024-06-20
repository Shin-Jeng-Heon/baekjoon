N, k = map(int,input().split())

factors = []

for i in range(1, N+1):
    if N%i == 0:
        factors.append(i)

if k <= len(factors):
    result = (factors[k - 1])
else:
    result = 0

print(result)