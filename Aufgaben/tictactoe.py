playerX = True
field = []
for i in range(10):
    field.append(str(i))
    
def print_field():
    for i in range(1, 10):
        if i % 3 == 0:
            print(field[i])
        else:
            print(field[i] + "|", end="")

def nextMove(playerX):
    while True:
        move = int(input("Enter your move (1-9): "))
        if move <=9 and field[move] == "X" or "O":
            if playerX:
                field[move] = "X"
            else:
                field[move] = "O"
        else:   
            print("Invalid move. Choose another one.")
            continue
        break

def winCon():
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        [1, 5, 9], [3, 5, 7]              
    ]
    
    for condition in win_conditions:
        if field[condition[0]] == field[condition[1]] == field[condition[2]] and field[condition[0]] != str(condition[0]):
            return True
    return False


while not winCon():
    print_field()
    nextMove(playerX)
    playerX = not playerX

if winCon() == True:
    print_field()
    if playerX:
        print("Player O wins!")
    else:
        print("Player X wins!")