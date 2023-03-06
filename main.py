def chess(x1,y1,x2,y2):
    door = False
    if x1 == x2 or y1 == y2:
        #straight
        door = True
    elif (y2-y1)/(x2-x1) == 1:
        #diagonal
        door = True
    elif abs(y2 - y1) == 2 and abs(x2-x1) == 1:
        door = True
    elif abs(y2 - y1) == 1 and abs(x2-x1) == 2:
        door = True
    return door

print(chess(4,3,7,6))