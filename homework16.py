lst = list(map(float, input("Введіть список чисел через кому: ").split(',')))
new_lst = []

for i in range(len(lst) - 1):
    new_lst.append(lst[i])
    average = (lst[i] + lst[i+1]) / 2
    new_lst.append(average)

new_lst.append(lst[-1])

print("Результат:", new_lst)