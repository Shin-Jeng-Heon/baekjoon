N = int(input())
s = list(map(int,input().split()))
max = s[0]
min = s[0]
for i in range(0, len(s)):
    if s[i] > 1000000 or s[i] < -1000000:
        exit()
    else:
        if max < s[i]:
            max = s[i]
        if min > s[i]:
            min = s[i]
print(min, max)