min_width = int(input("Enter minimal width: "))
max_width = int(input("Enter maximal width: "))

if min_width > max_width or (max_width - min_width) % 2 != 0:
    print("Warning: Invalid input.")
else:
    for i in range(min_width, max_width + 1, 2):
        if i == min_width:
            print(' ' * ((max_width - i) // 2) + '*' * i + ' ' * ((max_width - i) // 2))
        else:
            print(' ' * ((max_width - i) // 2) + '*' + ' ' * (i - 2) + '*' + ' ' * ((max_width - i) // 2))

    for i in range(max_width - 2, min_width - 1, -2):
        if i == min_width:
            print(' ' * ((max_width - i) // 2) + '*' * i + ' ' * ((max_width - i) // 2))
        else:
            print(' ' * ((max_width - i) // 2) + '*' + ' ' * (i - 2) + '*' + ' ' * ((max_width - i) // 2))
