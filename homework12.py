string = input('string = ')
sentences = string.split('. ')
formatted_result = ''
for sentence in sentences:
    words_with_double_o = [word.capitalize() for word in sentence.split() if word.lower().count('o') == 2]
    if words_with_double_o:
        formatted_result += ' '.join(words_with_double_o)
        formatted_result += '. ' if sentence != sentences[-1] else '. '

formatted_result = formatted_result.rstrip('. ')
print(f"Result: {formatted_result}")
