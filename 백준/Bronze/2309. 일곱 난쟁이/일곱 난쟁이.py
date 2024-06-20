list_a = []
sum = 0
for i in range(1,10):
    a = int(input())
    list_a.append(a)
    sum = sum + a

list_a.sort()

correct = []

for i in range(len(list_a)):
    for j in range(i+1,len(list_a)):
        if sum-(list_a[i] + list_a[j]) == 100:
            for k in range(len(list_a)):
                if k == i or k == j:
                    pass
                else:
                    print(list_a[k])
            exit()