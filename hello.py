a, b = [int(i) for i in input().split()], []
if len(a) == 1:
    b.append(a[0])
else:
    for i in a:
        if i == a[-1]:
            b.append(a[0] + a[a.index(i)-1])
        else:
            b.append(a[a.index(i)+1] + a[a.index(i)-1])
print(*b)