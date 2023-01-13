def print_func(not_arrived_guest_data):
    print(len(not_arrived_guest_data))

    for guest in sorted(not_arrived_guest_data):
        print(guest)


reservation_guests_list = set([input() for n in range(int(input()))])
arrived_guests_list = set()

current_guest = input()
while current_guest != "END":
    arrived_guests_list.add(current_guest)

    current_guest = input()

not_arrived_guests = reservation_guests_list.difference(arrived_guests_list)

print_func(not_arrived_guests)
