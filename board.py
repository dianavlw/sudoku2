board = [
    [6,1,9,0,3,0,0,4,0],
    [2,7,0,0,6,1,0,0,8],
    [0,0,0,0,4,7,6,2,1],
    [4,8,6,3,0,2,0,7,9],
    [0,0,0,0,1,4,5,8,0],
    [0,3,1,0,0,9,0,6,0],
    [0,0,5,7,2,0,8,0,6],
    [3,2,0,1,0,6,0,5,7],
    [1,6,0,4,0,0,0,3,0]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j !=0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(board)
