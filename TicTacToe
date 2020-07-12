print("Tic Tac Toe starts")

TicTacToe = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
for row in TicTacToe:
    print(row)

max = 9
count = 0
while count < max :
    x, y = input("Enter Coordination: ").split()
    if (int(x) <= 0) or (int(x) > 3) or (int(y) <= 0) or (int(y) > 3) :
        print('Please Fill 1 or 2 or 3 Only!')
    else:
        xx = int(x)-1
        yy = int(y)-1
        if TicTacToe[xx][yy] == ' ' :
            if ((count + 1) % 2) == 1 :
                TicTacToe[xx][yy] = 'o'
            else:
                TicTacToe[xx][yy] = 'x'
            for row in TicTacToe:
                print(row)
            count = count + 1
        else:
            print('Fill Coordination Again')

    if (TicTacToe[0][0] == 'x' and TicTacToe[0][1] == 'x' and TicTacToe[0][2] == 'x'):
        print('Winner is x')
        count = 9
    elif (TicTacToe[1][0] == 'x' and TicTacToe[1][1] == 'x' and TicTacToe[1][2] == 'x'):
        print('Winner is x')
        count = 9
    elif (TicTacToe[2][0] == 'x' and TicTacToe[2][1] == 'x' and TicTacToe[2][2] == 'x'):
        print('Winner is x')
        count = 9
    elif (TicTacToe[0][0] == 'x' and TicTacToe[1][1] == 'x' and TicTacToe[2][2] == 'x'):
        print('Winner is x')
        count = 9
    elif (TicTacToe[0][2] == 'x' and TicTacToe[1][1] == 'x' and TicTacToe[2][0] == 'x'):
        print('Winner is x')
        count = 9
    elif (TicTacToe[0][0] == 'x' and TicTacToe[1][0] == 'x' and TicTacToe[2][0] == 'x'):
        print('Winner is x')
        count = 9
    elif (TicTacToe[0][1] == 'x' and TicTacToe[1][1] == 'x' and TicTacToe[2][1] == 'x'):
        print('Winner is x')
        count = 9
    elif (TicTacToe[0][2] == 'x' and TicTacToe[1][2] == 'x' and TicTacToe[2][2] == 'x'):
        print('Winner is x')
        count = 9
    elif (TicTacToe[0][0] == TicTacToe[0][1] == TicTacToe[0][2] == 'o'):
        print('Winner is o')
        count = 9
    elif (TicTacToe[1][0] == TicTacToe[1][1] == TicTacToe[1][2] == 'o'):
        print('Winner is o')
        count = 9
    elif (TicTacToe[2][0] == TicTacToe[2][1] == TicTacToe[2][2] == 'o'):
        print('Winner is o')
        count = 9
    elif (TicTacToe[0][0] == TicTacToe[1][1] == TicTacToe[2][2] == 'o'):
        print('Winner is o')
        count = 9
    elif (TicTacToe[0][2] == TicTacToe[1][1] == TicTacToe[2][0] == 'o'):
        print('Winner is o')
        count = 9
    elif (TicTacToe[0][0] == TicTacToe[1][0] == TicTacToe[2][0] == 'o'):
        print('Winner is o')
        count = 9
    elif (TicTacToe[0][1] == TicTacToe[1][1] == TicTacToe[2][1] == 'o'):
        print('Winner is o')
        count = 9
    elif (TicTacToe[0][2] == TicTacToe[1][2] == TicTacToe[2][2] == 'o'):
        print('Winner is o')
        count = 9
