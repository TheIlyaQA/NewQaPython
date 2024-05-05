lst = list(map(int, input("Введіть список цілих чисел через кому: ").split(',')))
MIN = int(input("Введіть мінімальне значення: "))
MAX = int(input("Введіть максимальне значення: "))

filtered_list = [num for num in lst if MIN <= num <= MAX]

if filtered_list:
    sum_ = sum(filtered_list)
    product = 1
    for num in filtered_list:
        product *= num
    print("sum =", sum_, ", product =", product)
else:
    print("sum = None, product = None")
