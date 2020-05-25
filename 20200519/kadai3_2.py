print('数字を10個入力してください。')
odds = []
evens = []
for i in range(1,11):
    N = input(f'{i}つ目: ')
    if int(N)%2 == 0:
        evens.append(N)
    else:
        odds.append(N)
print(f'偶数: {",".join(evens)}')
print(f'偶数: {",".join(odds)}')
