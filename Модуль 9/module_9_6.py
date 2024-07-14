def all_variants(text):
    for length_of_combination in range(len(text)):
        for index in range(len(text)):
            result = ''
            if index < len(text) - length_of_combination:
                while len(result) <= length_of_combination:
                    result += text[index]
                    index += 1
                yield result


a = all_variants("abc")
for i in a:
    print(i)
