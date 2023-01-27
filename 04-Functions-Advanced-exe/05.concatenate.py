def concatenate(*strings, **text_elements):
    text = ''.join(strings)

    for key, value in text_elements.items():
        if key in text:
            text = text.replace(key, value)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
