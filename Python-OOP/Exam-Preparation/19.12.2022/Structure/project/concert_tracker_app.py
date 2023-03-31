from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if name == musician.name:
                raise Exception(f"{name} is already a musician!")

        if musician_type == "Guitarist":
            musician = Guitarist(name, age)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
        else:
            musician = Singer(name, age)

        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band_names = [b.name for b in self.bands]
        if name in band_names:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if place == concert.place:
                raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{concert.genre} concert in {concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = [m for m in self.musicians if m.name == musician_name][0]

        if not musician.name:
            raise Exception(f"{musician_name} isn't a musician!")

        band = [b for b in self.bands if b.name == band_name][0]

        if not band.name:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]

        if not band.name:
            raise Exception(f"{band_name} isn't a band!")

        musician = [m for m in band.members if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician[0])

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]

        singers = [m for m in band.members if isinstance(m, Singer)]
        drummers = [m for m in band.members if isinstance(m, Drummer)]
        guitarists = [m for m in band.members if isinstance(m, Guitarist)]

        if not singers and not drummers and not guitarists:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        is_singer_have_skills = True
        for singer in singers:
            if concert.genre == 'Rock':
                if 'sing high pitch notes' not in singer.skills:
                    is_singer_have_skills = False
            elif concert.genre == 'Metal':
                if 'sing low pitch notes' not in singer.skills:
                    is_singer_have_skills = False
            else:
                if 'sing low pitch notes' not in singer.skills and 'sing high pitch notes' not in singer.skills:
                    is_singer_have_skills = False

        is_drummer_have_skills = True
        for drummer in drummers:
            if concert.genre == 'Rock':
                if 'play the drums with drumsticks' not in drummer.skills:
                    is_drummer_have_skills = False
            elif concert.genre == 'Metal':
                if 'play the drums with drumsticks' not in drummer.skills:
                    is_drummer_have_skills = False
            else:
                if 'play the drums with drum brushes' not in drummer.skills:
                    is_drummer_have_skills = False

        is_guitarist_have_skills = True
        for guitarist in guitarists:
            if concert.genre == 'Rock':
                if 'play rock' not in guitarist.skills:
                    is_guitarist_have_skills = False
            elif concert.genre == 'Metal':
                if 'play metal' not in guitarist.skills:
                    is_guitarist_have_skills = False
            else:
                if 'play jazz' not in guitarist.skills:
                    is_guitarist_have_skills = False

        if not is_singer_have_skills and not is_drummer_have_skills and not is_guitarist_have_skills:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        concert_profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {concert_profit:.2f}$ from the {concert.genre} concert in {concert.place}."
