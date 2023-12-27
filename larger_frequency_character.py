def larger_frequency_character():
    input_string = "This is my          India"
    y = input_string.lower()
    dict ={}

    for x in y:
        if x.isalpha():
            if x in dict:
                dict[x] = dict[x] + 1
            else:
                dict[x] = 1

    max_character = ''
    max_count = 0
    for x, count in dict.items():
        if count > max_count:
            max_character = x
            max_count = count

    return f"{max_character} = {max_count}"

result = larger_frequency_character()

print(result)

