from os import system
from random import randint

ry=randint(0,9)
rx=randint(0,9)

gm=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

gm[ry][rx]= 1

################### map ######################
while True:

    system("cls")
    print("#"*20)
    for y in range(10):
        for x in range(10):
            if gm[y][x]==1:
                print("R","", end="")
            elif gm[y][x]==2:
                print("X","", end="")
            elif gm[ry][rx]==gm[3][3]:
                print("💥", end="")
            else:
                print( ".","", end="")
        print()
    print("#"*20)
    ################ map ######################
    ###########################################
    if gm[ry][rx]==gm[3][3]:
        print("Boom!!!Game over!!!")
        break

    option = input(">>> ")


    gm[ry][rx]= 0

    if option == 'd':
        rx +=1
    if option == 'a':
        rx -=1
    if option == 's':
        ry +=1
    if option == 'w':
        ry -=1


    gm[ry][rx]= 1

