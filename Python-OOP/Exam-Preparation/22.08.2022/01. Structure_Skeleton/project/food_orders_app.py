from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str) -> str:
        client = self.__get_client(client_phone_number)
        if client:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)

        return f"Client {client_phone_number} registered successfully."

    def __get_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, Starter) or isinstance(meal, MainDish) or isinstance(meal, Dessert):
                self.menu.append(meal)

    def show_menu(self) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        meals_in_menu = ''
        for meal in self.menu:
            meals_in_menu += meal.details() + "\n"

        return meals_in_menu.rstrip('\n')

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)

        for meal_name, qty in meal_names_and_quantities.items():
            meal = [m for m in self.menu if m.name == meal_name]
            if not meal:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal[0].quantity < qty:
                raise Exception(f"Not enough quantity of {meal[0].__class__.__name__}: {meal_name}")

        for meal_name, qty in meal_names_and_quantities.items():
            meal_menu = [m for m in self.menu if m.name == meal_name][0]
            client.shopping_cart.append(meal_menu)
            client.bill += meal_menu.price * qty
            meal_menu.quantity -= qty
            client.ordered_meal_quantities[meal_name] = qty

        meal_names = ', '.join([m.name for m in client.shopping_cart])

        return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal_name, qty in client.ordered_meal_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += qty

        client.shopping_cart = []
        client.bill = 0
        client.ordered_meal_quantities = {}

        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0.0
        client.ordered_meal_quantities = {}

        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money}\
                was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
