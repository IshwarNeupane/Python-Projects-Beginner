row1 = ["😂", "😂", "😂"]
row2 = ["😂", "😂", "😂"]
row3 = ["😂", "😂", "😂"]
map = [row1, row2, row3]
position = input("Where do you want to put treasure?")
# For position e.g. 23, 31, 12, etc, its a string (column*row).column is index 0 and row is index 1.
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
