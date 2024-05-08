# email = input("Enter an email address: ")
# if '@' not in email or '.' not in email or email.index('@') > email.index('.'):
#     print(f"email = {email} # False")
#     exit()
# if email.startswith('@') or email.endswith('.'):
#     print(f"email = {email} # False")
#     exit()
# for char in email:
#     if char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.':
#         print(f"email = {email} # False")
#         exit()
# if email.count('@') != 1 or email.count('.') != 1:
#     print(f"email = {email} # False")
#     exit()
# print(f"email = {email} # True")

# Updated version

email = input("Enter an email address: ")
valid = True

if ('@' not in email or '.' not in email or email.index('@') > email.index('.') or
        email.startswith('@') or email.endswith('.') or
        not all(char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.' for char in email) or
        email.count('@') != 1 or email.count('.') != 1):
    valid = False

if valid:
    print(f"email = {email} # True")
else:
    print(f"email = {email} # False")


# Test cases
# ("aaa@bbb.ccc")  # True
# ("invalid@@example.com")  # False
# ("noat.com")  # False
# "@domain.com")  # False
# ("user@domain")  # False
# ("user@domain.")  # False