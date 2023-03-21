def vowel_filter(function):
    def wrapper():
        vowel = ['a', 'e', 'i', 'o', 'u', 'y']
        func_data = function()
        result = [el for el in func_data if el.lower() in vowel]

        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
