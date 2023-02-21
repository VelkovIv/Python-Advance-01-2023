def palindrome(text, left_index, right_index=-1):
    if left_index == len(text) // 2:
        return f'{text} is a palindrome'

    if text[left_index] != text[right_index]:
        return f'{text} is not a palindrome'

    return palindrome(text, left_index + 1, right_index - 1)


print(palindrome("abcba", 0))
