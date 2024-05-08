longest_line = ""
with open("your_file", "r") as file:
    for line in file:
        line = line.rstrip()
        if len(line) >= len(longest_line):
            longest_line = line
print(longest_line)
