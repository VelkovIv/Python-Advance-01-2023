import unittest
from unittest import TestCase

from project.shopping_cart import ShoppingCart


class TestShippingCard(TestCase):

    def setUp(self) -> None:
        self.shopping_card = ShoppingCart('Shop', 100)

    def test_initialization(self):
        self.assertEqual(self.shopping_card.shop_name, "Shop")
        self.assertEqual(self.shopping_card.budget, 100)
        self.assertEqual(self.shopping_card.products, {})

    def test_shop_name_start_with_lower_letter_raising_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_card = ShoppingCart('shop', 100)
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_shop_name_contain_not_only_letter_raising_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_card = ShoppingCart('Shop1', 100)
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_card_costly_product_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_card.add_to_cart('Product1', 120)
        self.assertEqual(str(ve.exception), "Product Product1 cost too much!")

    def test_add_to_card_product_(self):
        res = self.shopping_card.add_to_cart('Product', 80)
        self.assertEqual("Product product was successfully added to the cart!", res)
        self.assertEqual(self.shopping_card.products['Product'], 80)
        self.shopping_card.add_to_cart('Product1', 20)
        self.assertEqual({'Product': 80, 'Product1': 20}, self.shopping_card.products)

    def test_remove_from_card_missing_product_raise_value_error(self):
        self.shopping_card.add_to_cart('Product', 80)
        with self.assertRaises(ValueError) as ve:
            self.shopping_card.remove_from_cart('Product1')
        self.assertEqual("No product with name Product1 in the cart!", str(ve.exception))

    def test_remove_from_card_product(self):
        self.shopping_card.add_to_cart('Product', 80)
        res = self.shopping_card.remove_from_cart('Product')
        self.assertEqual(self.shopping_card.products, {})
        self.assertEqual("Product Product was successfully removed from the cart!", res)

    def test__add__adding_other_shopping_card_instance(self):
        self.shopping_card.add_to_cart('Product', 80)
        new_card = ShoppingCart('New', 1000)
        new_card.add_to_cart('Product1', 50)
        merged = self.shopping_card.__add__(new_card)
        self.assertEqual('ShopNew', merged.shop_name)
        self.assertEqual(1100, merged.budget)
        self.assertEqual({'Product': 80, 'Product1': 50}, merged.products)

    def test_buy_products_with_amonth_bigger_than_bidget_raise_value_error(self):
        self.shopping_card.add_to_cart('Product', 80)
        self.shopping_card.add_to_cart('Product1', 50)
        with self.assertRaises(ValueError) as ve:
            self.shopping_card.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 30.00lv!", str(ve.exception))


    def test_buy_products_with_amonth_lower_than_bidget(self):
        self.shopping_card.add_to_cart('Product', 30)
        self.shopping_card.add_to_cart('Product1', 50)
        res = self.shopping_card.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 80.00lv.", res)


if __name__ == '__main__':
    unittest.main()
