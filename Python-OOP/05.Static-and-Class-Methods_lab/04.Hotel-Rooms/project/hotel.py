from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = self.find_room_by_number(room_number)
        results = room.take_room(people)
        if results:
            return results
        self.guests += people

    def free_room(self, room_number: int):
        room = self.find_room_by_number(room_number)
        room_guests = room.guests
        results = room.free_room()
        if results:
            return results
        self.guests -= room_guests

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        results = f"Hotel {self.name} has {self.guests} total guests\n" + \
                  f"Free rooms: {', '.join(free_rooms)}\n" + \
                  f"Taken rooms: {', '.join(taken_rooms)}"
        return results

    def find_room_by_number(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room
