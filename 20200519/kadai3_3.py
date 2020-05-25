qq = [[str(i*j).rjust(2) for j in range(1, 10)] for i in range(1, 10)]
for q in qq:
    print(*q)
