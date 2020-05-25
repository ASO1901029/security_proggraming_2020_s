print("数字を10個入力してください。")
numbers = []
for i in range(1, 11):
    numbers.append(input(f'{i}つ目: '))
print('入力された10個の数字を表示します。')
for n in numbers:
    print(n)
