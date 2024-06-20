sum = 0
high = 0

for i in range(1, 11):
    a, b = map(int, input().split())
    if i == 1:
        a = 0
    if i == 10:
        b = 0

    sum = sum + b - a

    if  sum < 0 or sum > 10000:
        exit()


    if sum > high:
        high = sum

print(high)