sentences = input("Enter your sentences here: ")
word_counts = []
sentence = ""

for char in sentences:
    if char == '.':
        if sentence:
            words = sentence.strip().split()
            word_counts.append(len(words))
            sentence = ""
    else:
        sentence += char

if sentence:
    words = sentence.strip().split()
    word_counts.append(len(words))

print(f"words_number -> {word_counts}")