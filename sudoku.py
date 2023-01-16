bod = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
]
def makeboard(bod):
    for i in range(len(bod)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - - -")
        
        for j in range(len(bod[0])):
            if j%3==0 and j!=0:
                print(" | ", end=" ")
            if j==8:
                print(bod[i][j])  
            else:
                print(str(bod[i][j]) + " ", end = " ")  
def find_empty(bod):
    for i in range(len(bod)):
        for j in range(len(bod[0])):
            if bod[i][j]==0:
                return(i, j)
    return None

def valid(bod, number, place):
    #check row
    for i in range(len(bod[0])):
        if bod[place[0]][i] ==number and place[1]!=i:
            return False
    #check column
    for j in range(len(bod[0])):
        if bod[j][place[1]]== number and place[0]!=j:
            return False
    #check box
    x_box = place[0]//3
    y_box = place[1]//3

    for i in range(x_box*3, x_box*3 +3):
        for j in range(y_box*3, y_box*3 + 3):
            if bod[i][j] == number and (i,j) !=place: 
                return False
    return True

def solveprob(bod):
    find = find_empty(bod)
    if not find:
        return True
    else:
        row, column = find
    for i in range(1,10):
        if valid(bod, i, (row, column)):
            bod[row][column]= i

            if solveprob(bod):
                return True
            bod[row][column] = 0

    return False

makeboard(bod)
solveprob(bod)
print("-------------------")
makeboard(bod)