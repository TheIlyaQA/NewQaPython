input_list = list(map(int, input("Enter a list of integers separated by commas: ").split(',')))

divisible_by_3_not_5 = [num for num in input_list if num % 3 == 0 and num % 5 != 0]
divisible_by_5_not_3 = [num for num in input_list if num % 5 == 0 and num % 3 != 0]
divisible_by_3_and_5 = [num for num in input_list if num % 3 == 0 and num % 5 == 0]

print("Numbers divisible by 3, but not by 5:", divisible_by_3_not_5)
print("Numbers divisible by 5, but not by 3:", divisible_by_5_not_3)
print("Numbers divisible by both 3 and 5:", divisible_by_3_and_5)
