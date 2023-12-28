def larger_frequency_char_sym(input_string):
    y = input_string.lower()
    dict_alphabet ={}
    dict_non_alphabet ={}

    for x in y:
        if x.isalpha():
            if x in dict_alphabet:
                dict_alphabet[x] = dict_alphabet[x] + 1
            else:
                dict_alphabet[x] = 1

        elif not x.isspace():
            if x in dict_non_alphabet:
                dict_non_alphabet[x] = dict_non_alphabet[x] + 1
            else:
                dict_non_alphabet[x] = 1


    max_alphabetic_character = ''
    max_count_alphabetic_character = 0

    for x, count in dict_alphabet.items():
        if count > max_count_alphabetic_character:
            max_alphabetic_character = x
            max_count_alphabetic_character = count

    max_non_alphabetic_character = ''
    max_count_non_alphabetic_character = 0

    for x, count in dict_non_alphabet.items():
        if count > max_count_non_alphabetic_character:
            max_non_alphabetic_character = x
            max_count_non_alphabetic_character = count


    return f"Alphabetic: {max_alphabetic_character} = {max_count_alphabetic_character}," \
           f" Non-Alphabetic: {max_non_alphabetic_character} = {max_count_non_alphabetic_character}"
input_paragraph = """
There are many different kinds of animals that live in China. 
Tigers and leopards are animals that live in China's forests in the north. 
In the jungles, monkeys swing in the trees and elephants walk through the brush
"""
result_paragraph = larger_frequency_char_sym(input_paragraph)
print(result_paragraph)


