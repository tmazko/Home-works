from os import system
from time import sleep
from random import randint

#----------------Functions----------------------------
def el_in_cards(el, cards, size):
    for i in range(size):
        for j in range(size):
            if cards[i][j]==el:
                return True
    return False

def draw_cards(cards,cards_status, size, empty_el):
    print("----Train Your Brain----")
    print("    ", end="")
    for i in range(size):
        print(str(chr(65+i)), end=" ")
    print()
    print("  - ", end="")
    for i in range(size):
        print("—", end=" ")
    print()
    for i in range(size):
        for j in range(size):
            if j == 0:
                print(i + 1, end=" | ")
            if cards_status[i][j]=='O' or cards_status[i][j]=='G':
                print(cards[i][j], end=" ")
            else:
                print(empty_el, end=" ")
        print()
def check_winning(cards_status, size):
    for i in range(size):
        for j in range(size):
            if cards_status[i][j]!='G':
                return False
    return True
def validation(move,cards_status, size, cards_table):
    if (len(move)!=2):
        return False
    elif not el_in_cards(move, cards_table, size):
        return False
    i1,j1=find_indexes(cards_table,size,move)
    if cards_status[i1][j1]!='C':
        return False

    return True
def check_guessing(cards,cards_status, size, move1, move2):
    i1, j1 = find_indexes(cards_table, size, move1)
    i2, j2 = find_indexes(cards_table, size, move2)
    if cards[i1][j1]==cards[i2][j2]:
        cards_status[i1][j1]='G'
        cards_status[i2][j2] = 'G'
    else:
        cards_status[i1][j1] = 'C'
        cards_status[i2][j2] = 'C'
def find_indexes(array, size, el):
    indexes=[]
    for i in range(size):
        for j in range(size):
            if array[i][j]==el:
                indexes.append(i)
                indexes.append(j)
                return i,j

#--------------PRINT rules-----------------------------

print("**************************************************************************")
print("____________________Welcome to TRAIN TOUR BRAIN Game______________________")
print("----Rules-----------------------------------------------------------------")
print("1. You have a board of cards. Each card has a copy.")
print("2. You take turns opening 2 cards trying to find its copy.")
print("3. If the pair is guessed, it remains open, otherwise the cards are closed.")
print("4. The game ends when you find all the pairs.")
print("5 At the end you will find out how many moves you have spent.")
print("-------------------------------------------------------------------------")

#-------------------------CREATE DATA----------------------------------------

size=""
print("Choose the size of your board 4*4 or 6*6(enter 4 or 6):")
while size!="4" and size!="6":
    size=input(">>")
    size=size.replace(" ", "")
size=int(size)
empty_el='*'
cards=[]
move_counter=0

cards_status=[]
for i in range(size):
    cards_status.append(['C']*size)

for i in range(size):
    cards.append([empty_el]*size)

symbol=empty_el
while el_in_cards(empty_el,cards,size):
    if size==4:
        while el_in_cards(symbol,cards,size):
            symbol=chr(randint(65,90))
    else:
        ind=randint(0,1)
        if ind:
            symbol = chr(randint(65, 90))
        else:
            symbol = chr(randint(48, 57))
    row1=randint(0,size-1)
    column1=randint(0,size-1)
    row2 = randint(0, size-1)
    column2 = randint(0, size-1)
    if cards[row1][column1]==cards[row2][column2]==empty_el and (row1!=row2 or column1!=column2):
        cards[row1][column1] = symbol
        cards[row2][column2]=symbol

cards_table = []
for i in range(size):
    cards_table.append(["0"] * size)
for i in range(size):
    for j in range(size):
        cards_table[i][j] = str(chr(65 + j)) + str(i + 1)

#-------------------------------GAME LOGIC---------------------------------------------

while not check_winning(cards_status,size):
    move_counter += 1
    move1 = ""
    move2 = ""

    system("cls")
    draw_cards(cards, cards_status, size, empty_el)

    while not validation(move1, cards_status, size, cards_table):
        move1=input("Enter the position of the first card(a1 or A1): ")
        move1=move1.upper()
        move1=move1.replace(" ","")
    i1, j1 = find_indexes(cards_table, size, move1)
    cards_status[i1][j1]='O'

    system("cls")
    draw_cards(cards, cards_status, size, empty_el)

    while not validation(move2, cards_status, size, cards_table):
        move2=input("Enter the position of the second card(a1 or A1): ")
        move2=move2.upper()
    i2, j2 = find_indexes(cards_table, size, move2)
    cards_status[i2][j2] = 'O'

    system("cls")
    draw_cards(cards, cards_status, size, empty_el)
    sleep(2)
    if(check_guessing(cards, cards_status, size, move1, move2)):
        break

print("Congratulations! You did it!")
print("Number of moves:", move_counter)



