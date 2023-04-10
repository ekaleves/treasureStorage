# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Type 1, 2, or 3 for the row and 1, 2, or 3 for the position. (Exemple first item of the row 1 type: 11) :")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

rowNumber = int(position[0])
columnNumber = int(position[1])
treasure = "X"
if columnNumber == 1:
    if rowNumber == 1:
        row1[0] = "X"
    elif rowNumber == 2:
        row1[1] = "X"
    elif rowNumber == 3:
        row1[2] = "X"
    else:
        print("Please use 1, 2, or 3.")

elif columnNumber == 2:
    if rowNumber == 1:
        row2[0] = "X"
    elif rowNumber == 2:
        row2[1] = "X"
    elif rowNumber == 3:
        row2[2] = "X"
    else:
        print("Please use 1, 2, or 3.")

elif columnNumber == 3:
    if rowNumber == 1:
        row3[0] = "X"
    elif rowNumber == 2:
        row3[1] = "X"
    elif rowNumber == 3:
        row3[2] = "X"
    else:
        print("Please use 1, 2, or 3.")
    
else:
    print("Please use 1, 2, or 3.")





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

