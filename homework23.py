def second_largest_number(nums):
    if len(nums) < 2:
        return None

    largest = second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None
    else:
        return second_largest


# Test cases
print(second_largest_number([]))  # None
print(second_largest_number([1, 1]))  # None
print(second_largest_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 9
