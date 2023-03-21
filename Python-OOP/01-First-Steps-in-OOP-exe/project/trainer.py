# from pokemon import Pokemon
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)

            return f"Caught {Pokemon.pokemon_details(pokemon)}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        # try:
        #     pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        #
        # except StopIteration:
        #     return f"Pokemon is not caught"
        #
        # self.pokemons.remove(pokemon)
        #
        # return f"You have released {pokemon_name}"
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        pokemons_data = '\n'.join(f"- {p.pokemon_details()}" for p in self.pokemons)

        return f"Pokemon Trainer {self.name}\n" + \
            f"Pokemon count {len(self.pokemons)}\n" + \
            pokemons_data


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
