#Method 1
str1 = input("Enter a string: ")
str2 = str1[::-1]
print(f"Method 1 -> \"{str1}\" # {str1.lower().strip() == str2.lower().strip()}")
#Method 2
str3 = input("Enter a string: ")
print(f"Method 2 -> \"{str3}\" # {str3.lower().strip() == ''.join(reversed(str3.lower().strip()))}")