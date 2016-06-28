import random
import os
import msvcrt

Cube = [[2,0,0,0],
        [0,0,0,2],
        [0,0,0,0],
        [0,0,0,0]]


def SameLecngthFunc(x):
    if x==0:        return '    '
    elif x<=9:        return '  '+str(x)+' '
    elif x<=99:     return ' '+str(x)+' '
    elif x<=999:    return ' '+str(x)
    elif x<=9999:   return str(x)

def DisplayGrid(Cube):

    GridWidth  = 4
    GridHeight = 4
    for Row in range(0,(GridHeight*4)+5):
        print '\n    ',
        if (Row%(GridHeight+1)) == 0:
            for width in range(0,(GridWidth*4)+5):
                print "-",
        else:
            for width in range(0,(GridWidth*4)+5):
                if (width%(GridWidth+1)) == 0:
                    print '|',
                else:
                    ElementCol = width/(GridWidth+1)
                    ElementRow = Row/(GridWidth+1)
                    GridSpaceX = width%(GridWidth+1)
                    GridSpaceY = Row%(GridWidth+1)
                    if GridSpaceX == 1:
                        if GridSpaceY == 3: print ' '+SameLecngthFunc(Cube[ElementRow][ElementCol])+'  ',
                        else: print '       ',

DisplayGrid(Cube)
"""def ShiftAndAdd(Row):
    Row = [Ele for Ele in Row if Ele !=0]
    Row=Row+[0]*(4-len(Row))
    for i in range(0,3):
        if (Row[i]==Row[i+1]):
            Row[i]=Row[i]+Row[i+1]
            Row[i+1:]=Row[i+2:]+[0]
    return Row

def getRow(Cube,Rowno):
    return Cube[Rowno-1]

def getColumn(Cube,Colno):
    return [Row[Colno-1]for Row in Cube]

def setRow(Cube,Rowno,NewVal):
    Cube[Rowno-1]=NewVal
    return Cube

def setColumn(Cube,Colno,NewVal):
    for Row in range(0,len(Cube)):
        Cube[Row][Colno-1]=NewVal[Row]
    return Cube





def playMove(Cube,Move):
    for Every in range(1,5):
        if Move=='L':
            beforeMove=getRow(Cube,Every)
            afterMove=ShiftAndAdd(beforeMove)
            Cube= setRow(Cube,Every,afterMove)
        elif Move=='R':
            beforeMove=getRow(Cube,Every)[-1::-1]
            afterMove=ShiftAndAdd(beforeMove)[-1::-1]
            Cube= setRow(Cube,Every,afterMove)
        elif Move=='D':
            beforeMove=getColumn(Cube,Every)[-1::-1]
            afterMove=ShiftAndAdd(beforeMove)[-1::-1]
            Cube= setColumn(Cube,Every,afterMove)
        elif Move=='U':
            beforeMove=getColumn(Cube,Every)
            afterMove=ShiftAndAdd(beforeMove)
            Cube= setColumn(Cube,Every,afterMove)

    return Cube

def GetFreeGrids(Cube):
    FreeGrid = []
    for i in range(0,4):
        for j in range(0,4):
            if Cube[i][j]==0:
                FreeGrid.append((i*4)+j)
    return FreeGrid



def AddEle(Cube,Loc,Value):
    Cube[Loc/4][Loc%4]=Value
    return Cube

while 1:
    os.system('cls')
    DisplayGrid(Cube)
    #Myinput=raw_input("Enter move").upper()
    Myinput=(msvcrt.getch()).upper()
    if ord(Myinput) in [75,77,72,80]:
        Map={75:'L',77:'R',72:'U',80:"D"}
        Myinput=Map[ord(Myinput)]
    if not Myinput in ['R','L',"U",'D','Q']:
        print "Give valid i/p"
        continue
    if Myinput=='Q':
        print "Game quited"
        break
    Cube=playMove(Cube,Myinput)
    FreeGrids=GetFreeGrids(Cube)
    if FreeGrids:
        Loc=random.sample(FreeGrids,1)[0]
        Value=random.sample([2,4],1)[0]
        Cube=AddEle(Cube,Loc,Value)
    else:
        print "You lost"
        break

raw_input()

"""
