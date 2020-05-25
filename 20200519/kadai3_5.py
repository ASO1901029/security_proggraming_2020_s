def sort(ls: list):
    rank_ls = [0] * len(ls)
    for i in range(len(ls) - 1):
        for j in range(i + 1, len(ls)):
            if ls[i] > ls[j]:
                rank_ls[i] += 1
            else:
                rank_ls[j] += 1
    rt_ls = [0] * len(ls)
    for i in range(len(ls)):
        rt_ls[rank_ls[i]] = ls[i]
    return rt_ls

print("数字を10個入力してください。")
numbers = []
for i in range(1, 11):
    numbers.append(int(input(f'{i}つ目: ')))

sorted_numbers = sort(numbers)
print(sorted_numbers)
