def lst2dict(lst):
    dictionary = {}
    for i in range(0, len(lst) - 1, 2):
        dictionary[lst[i]] = lst[i + 1]
    return dictionary

# Test cases
print(lst2dict([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(lst2dict(['a', 'A', 'b', 'B', 'c', 'f', 'g', 'h']))



