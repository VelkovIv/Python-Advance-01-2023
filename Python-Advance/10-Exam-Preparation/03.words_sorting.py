def words_sorting(*words):
    words_dict = {}
    result = ''
    total_value = 0

    for word in words:
        word_value = 0
        for char in word:
            word_value += int(ord(char))
        words_dict[word] = word_value

    for value in words_dict.values():
        total_value += value

    if total_value % 2 == 0:
        for k, v in sorted(words_dict.items(), key=lambda item: item[0]):
            result += f'{k} - {v}\n'
    else:
        for k, v in sorted(words_dict.items(), key=lambda item: item[1], reverse=True):
            result += f'{k} - {v}\n'

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
