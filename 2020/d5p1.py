import math
seats = [str(x).strip() for x in open("Inputs/d5").readlines()]
seats_array = []
for seat in seats:
    seat = seat.translate("".maketrans("FBLR", "0101"))
    seat = int(seat, 2)
    seats_array.append(seat)

seats_array.sort()

print(max(seats_array))

print((sum(range(min(seats_array), max(seats_array)+1))) - sum(seats_array))