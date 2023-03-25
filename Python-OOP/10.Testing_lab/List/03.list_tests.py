from List.extended_list import IntegerList
import unittest


class IntegerListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3, 4, 5.5, 6, 8, 10.454, 'abc', ['a', 1])

    def test_integer_list_constructor(self):
        result = [1, 2, 3, 4, 6, 8]
        self.assertEqual(self.integer_list.get_data(), result)

    def test_adding_int_element_to_integer_list_(self):
        element = 20
        self.integer_list.add(element)
        result = [1, 2, 3, 4, 6, 8, 20]
        self.assertEqual(self.integer_list.get_data(), result)

    def test_adding_not_int_element_to_integer_list_(self):
        element = 'A'
        with self.assertRaises(ValueError) as context:
            self.integer_list.add(element)
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_removing_int_element_from_integer_list(self):
        idx = 2
        self.integer_list.remove_index(idx)
        result = [1, 2, 4, 6, 8]
        self.assertEqual(self.integer_list.get_data(), result)

    def test_integer_list_raising_index_error(self):
        idx = 10
        with self.assertRaises(IndexError) as context:
            self.integer_list.remove_index(idx)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_element_from_integer_list(self):
        idx = 2
        self.assertEqual(self.integer_list.get(idx), 3)

    def test_get_element_from_integer_list_raise_index_error(self):
        idx = 20
        with self.assertRaises(IndexError) as context:
            self.integer_list.get(idx)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_int_into_integer_list(self):
        idx = 4
        element = 5
        result = [1, 2, 3, 4, 5, 6, 8]
        self.integer_list.insert(idx, element)
        self.assertEqual(self.integer_list.get_data(), result)

    def test_insert_element_into_integer_list_raise_index_error(self):
        idx = 40
        element = 5
        with self.assertRaises(IndexError) as context:
            self.integer_list.insert(idx, element)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_element_into_integer_list_raise_value_error(self):
        idx = 4
        element = 5.5
        with self.assertRaises(ValueError) as context:
            self.integer_list.insert(idx, element)
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(self.integer_list.get_biggest(), 8)

    def test_get_index(self):
        idx = 6
        self.assertEqual(self.integer_list.get_index(idx), 4)


if __name__ == '__main__':
    unittest.main()
