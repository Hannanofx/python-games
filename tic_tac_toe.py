def check(pos,ps,player):
    if (ps[0]!='-' and ps[0]==ps[1] and ps[1]==ps[2]) or (ps[3]!='-' and ps[3]==ps[4] and ps[4]==ps[5]) or (ps[6]!='-' and ps[6]==ps[7] and ps[7]==ps[8]):
        print(f"Player {player} won")
        exit(0)
    elif (ps[0]!='-' and ps[0]==ps[3] and ps[3]==ps[6]) or (ps[1]!='-' and ps[1]==ps[4] and ps[4]==ps[7]) or (ps[2]!='-' and ps[2]==ps[5] and ps[5]==ps[8]):
        print(f"Player {player} won")
        exit(0)
    elif (ps[0]!='-' and ps[0]==ps[4] and ps[4]==ps[8]) or (ps[2]!='-' and ps[2]==ps[4] and ps[4]==ps[6]):
        print(f"Player {player} won")
        exit(0)

def inp(name):
     pos=int(input(f"{name}'s Turn. Enter position:"))
     return pos

def invalid(pos,ps,name,player):
    if pos-1>8 or pos-1<0:
        print("Invalid position")
        inp(name)
    else:
        if ps[pos-1]!='-':
            print("Already occupied")
            inp(name)
        else:
           ps[pos-1]=player
           return ps[pos-1]

#  MAIN
print("This is a TIC-TAC-TOE Game")
A=input("Enter player 'X' name:")
B=input("Enter player 'O' name:")
x='x'
o='o'
ps=['-','-','-','-','-','-','-','-','-']

for i in range(0,8,1):
    pos=inp(A)
    invalid(pos,ps,A,x)
    print(f" {ps[0]} | {ps[1]} | {ps[2]}")
    print("------------")
    print(f" {ps[3]} | {ps[4]} | {ps[5]}")
    print("------------")
    print(f" {ps[6]} | {ps[7]} | {ps[8]}")
    check(pos,ps,x)
    
    pos=inp(B)
    invalid(pos,ps,B,o)
    print(f" {ps[0]} | {ps[1]} | {ps[2]}")
    print("------------")
    print(f" {ps[3]} | {ps[4]} | {ps[5]}")
    print("------------")
    print(f" {ps[6]} | {ps[7]} | {ps[8]}")
    check(pos,ps,o)

# Checking draw
print("Game is Draw!!")
