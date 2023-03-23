def type_check(input_type):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, input_type):
                    return "Bad Type"

            return func(*args)

        return wrapper

    return decorator

a=1
@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))


# # test first zero
# import unittest
#
# class TypeCheckTests(unittest.TestCase):
#     def test_zero_first(self):
#         @type_check(int)
#         def times2(num):
#             return num*2
#         self.assertEqual(times2(2), 4)
#         self.assertEqual(times2('Not A Number'), 'Bad Type')
#
# if __name__ == '__main__':
#     unittest.main()