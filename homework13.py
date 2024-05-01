email = input("Enter an email address: ")
if '@' not in email or '.' not in email or email.index('@') > email.index('.'):
    print(f"email = {email} # False")
    exit()
if email.startswith('@') or email.endswith('.'):
    print(f"email = {email} # False")
    exit()
for char in email:
    if char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.':
        print(f"email = {email} # False")
        exit()
if email.count('@') != 1 or email.count('.') != 1:
    print(f"email = {email} # False")
    exit()
print(f"email = {email} # True")

# Test cases
# ("aaa@bbb.ccc"))  # True
# ("invalid@@example.com"))  # False
# ("noat.com"))  # False
# "@domain.com"))  # False
# ("user@domain"))  # False
# ("user@domain."))  # False