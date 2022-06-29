def show_B_board():
    for i in range(3):
        for j in range(3):
            print(B[i][j], end = ' ')
        print()

B = [["_","_","_"],
     ["_","_","_"],
     ["_","_","_"]]

show_B_board()

while True:
    print("player1")

    while True:
        row = int(input("Please type row : "))
        col = int(input("Please type column"))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if B[row][col]==' _ ':
                B [row][col]=" O "
                break
            else:
                print("This cell is not empty")
        else:
            print("Your answer is not defined for the game. Please try again:)")
    show_B_board()


    print("player2")

    while True:
        row = int(input("Please type row : "))
        col = int(input("Please type column"))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if B[row][col]==' _ ':
               B[row][col]=" X "
               break
            else:
                print("This cell is not empty")
        else:   
            print("Your answer is not defined for the game. Please try again:)")
    show_B_board()