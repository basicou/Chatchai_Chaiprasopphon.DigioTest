print('Start calculator program (If you want to stop the program, please fill \"end\"')
print('You can use + - * / only')
loop,checkequal,ans = 0,0,0
Variables = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
VarValues = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
countvar,lastvar,countcom,countoper = 0,0,0,0
operator = ''
NEquation = ''

while loop == 0 :
    Equation = input('Enter : ')
    Equation = Equation.replace(' ','')
    if Equation == 'end':
        loop = 1
    else :
        checkequal = Equation.count('=')
        if checkequal == 0 :
            if Equation.find('+') != -1:
                countoper = Equation.find('+')
                operator = '+'
            elif Equation.find('-') != -1:
                countoper = Equation.find('-')
                operator = '-'
            elif Equation.find('*') != -1:
                countoper = Equation.find('*')
                operator = '*'
            elif Equation.find('/') != -1:
                countoper = Equation.find('/')
                operator = '/'
            else:
                print('Operttion is + - * / only.')
            if Equation[0:countoper] in Variables :
                first = VarValues[Variables.index(Equation[0:countoper])]
            else :
                first = Equation[0:countoper]
            if Equation[countoper+1:len(Equation)] in Variables:
                secound = VarValues[Variables.index(Equation[countoper+1:len(Equation)])]
            else :
                secound = Equation[countoper+1:len(Equation)]
            NEquation = first+operator+secound
            print(eval(NEquation))
        elif checkequal == 1 : #Use in cast that generate variable
            if Equation[0:Equation.find('=')] in Variables: #Use in case that had same variable (old variable) in 'Variables'
                countvar = Variables.index(Equation[0:Equation.find('=')])
                Variables[countvar] = Equation[0:Equation.find('=')]
                VarValues[countvar] = Equation[Equation.find('=') + 1:len(Equation)]
                print(Variables)
                print(VarValues)
            else : #Use in case that new variable
                if lastvar == 9 :#Use in case that the number of variables are full
                    print(Variables)
                    print(VarValues)
                    lastvar = input('Please fill the position of new variable : ')
                else :
                    while Variables[lastvar] != ' ': #Count the number of variables which are filled in 'Variable'
                        lastvar = lastvar + 1
                countvar = int(lastvar)
                Variables[countvar] = Equation[0:Equation.find('=')]
                VarValues[countvar] = Equation[Equation.find('=')+1:len(Equation)]
                print(Variables)
                print(VarValues)
        else :
            print('Input again!')
