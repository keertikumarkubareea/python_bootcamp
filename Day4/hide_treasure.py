line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
treasure_map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where to hide it?: ")  # Where do you want to put the treasure?

row = int(position[1]) - 1
letter = position[0]
if letter == "A":
    column = 0
elif letter == "B":
    column = 1
else:
    column = 2

treasure_map[row][column] = 'X'

print(f"{line1}\n{line2}\n{line3}")
