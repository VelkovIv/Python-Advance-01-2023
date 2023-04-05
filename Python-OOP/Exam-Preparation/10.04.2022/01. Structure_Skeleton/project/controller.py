from typing import List
from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players):
        for player in players:
            if player not in self.players:
                self.players.append(player)
        return f"Successfully added: {', '.join(Player.PLAYER_NAMES)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return
        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        supply = self.find_last_supply(sustenance_type)

        if player.stamina < 100:
            if supply.energy + player.stamina > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy

            self.supplies.remove(supply)

            return f"{player_name} sustained successfully with {supply.name}."

        if sustenance_type == "Food":
            raise Exception("There are no food supplies left!")
        raise Exception("There are no drink supplies left!")

    def find_last_supply(self, sustenance_type: str):
        for i in range(len(self.supplies) - 1, -1, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                return self.supplies[i]

    def find_player(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.find_player(first_player_name)
        second_player = self.find_player(second_player_name)
        if first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        if second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if first_player.stamina > second_player.stamina:
            first_attacker = second_player
            second_attacker = first_player
        else:
            first_attacker = first_player
            second_attacker = second_player

        second_attacker.stamina -= first_attacker.stamina / 2
        first_attacker.stamina -= second_attacker.stamina / 2

        if first_player.stamina > second_player.stamina:
            if second_player.stamina < 0:
                second_player.stamina = 0

            return f"Winner: {first_player.name}"

        if first_player.stamina < 0:
            first_player.stamina = 0

        return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            supplies = self.food_supply_for_next_day()
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            if supplies:
                for supply in supplies:
                    player.stamina += supply.energy

    def food_supply_for_next_day(self):
        supplies = []

        for supply in self.supplies:
            if type(supply).__name__ == 'Food':
                if len(supplies) == 0:
                    supplies.append(supply)
                    self.supplies.remove(supply)
            else:
                if len(supplies) == 1:
                    supplies.append(supply)
                    self.supplies.remove(supply)

            if len(supplies) == 2:
                return supplies

    def __str__(self):
        players = '\n'.join([p.__str__() for p in self.players])
        supplies = '\n'.join([s.details() for s in self.supplies])
        return f'{players}\n{supplies}'
