from typing import List
from project.player import Player


class Team:
    def __init__(self, name: str, ratting: int):
        self.__name = name
        self.__rating = ratting

        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)

        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str:
        for player in self.__players:
            if player_name == player.name:
                self.__players.remove(player)
                return player

        return f"Player {player_name} not found"
