def larger_frequency_character():
    input_string = "This is my          India;;;;;;........"
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


    return f"Alphabetic: {max_alphabetic_character} = {max_count_alphabetic_character}, Non-Alphabetic: {max_non_alphabetic_character} = {max_count_non_alphabetic_character}"


result = larger_frequency_character()

print(result)