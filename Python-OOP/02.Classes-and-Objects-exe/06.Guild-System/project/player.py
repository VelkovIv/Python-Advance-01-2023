class Player:
    def __init__(self, name: str, hp: str, mp: str):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skill = {}  # skill as key and mana cost as value
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: str):
        if skill_name not in self.skill:
            self.skill[skill_name] = mana_cost

            return f"Skill {skill_name} added to the collection of the player {self.name}"

        return "Skill already added"

    def player_info(self):
        result = ''
        for s, m in self.skill.items():
            result += f'==={s} - {m}\n'

        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n" + result

