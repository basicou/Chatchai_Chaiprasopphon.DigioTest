import math
print('Read Score Exam')

Text = input('Text : ')
Split = Text.split()

CountS,CountP,CountA = 0,0,0
Words,Sentences,Characters,Syllables,Polysyllables = 0,0,0,0,0
ARI,FKGL,SMOG,CLI = 0,0,0,0
ARIAge,FKGLAge,SMOGAge,CLIAge,AverageAge = 0,0,0,0,0

Words = len(Split)
Sentences = Text.count('.') + Text.count('!') + Text.count('?')
Characters = len(Text)

while CountS < len(Text) :
    if (Text[CountS] in 'aeiouyAEIOUY') and (Text[CountS-1] not in 'aeiouyAEIOUY'):
        Syllables = Syllables + 1
    CountS = CountS + 1

while CountP < len(Split) :
    CountPS = 0
    TestPolysyllable = 0
    while CountPS < len(Split[CountP]):
        if (Split[CountP][CountPS] in 'aeiouyAEIOUY') and (Split[CountP][CountPS-1] not in 'aeiouyAEIOUY'):
            TestPolysyllable = TestPolysyllable + 1
        CountPS = CountPS + 1
    if TestPolysyllable >= 3 :
        Polysyllables = Polysyllables + 1
    CountP = CountP + 1

print('Words : ' + str(Words))
print('Sentences : ' + str(Sentences))
print('Characters : ' + str(Characters))
print('Syllables : ' + str(Syllables))
print('PolySyllables : ' + str(Polysyllables))
print('')

Approach = input('Enter 1 : Automated Readability Inder (ARI)\n'
                 'Enter 2 : Flesch-Kincaid Readability Tests (FKGL)\n'
                 'Enter 3 : Simple Measure of Gobbledygook (SMOG)\n'
                 'Enter 4 : Coleman-Liau Readability Index (GLI)\n'
                 'Enter all: 1-4\n'
                 'Enter the score you want to calculation : ').split()
if Approach[0] == 'all':
    Approach = ['1','2','3','4']
while CountA < len(Approach):
    if Approach[CountA] == '1':
        ARI = 4.71*(Characters/Words) + 0.5*(Words/Sentences) - 21.43
        if round(ARI) <= 1:
            ARIAge = 6;
        elif round(ARI) == 2:
            ARIAge = 7
        elif round(ARI) == 3:
            ARIAge = 9
        elif round(ARI) == 4:
            ARIAge = 10
        elif round(ARI) == 5:
            ARIAge = 11
        elif round(ARI) == 6:
            ARIAge = 12
        elif round(ARI) == 7:
            ARIAge = 13
        elif round(ARI) == 8:
            ARIAge = 14
        elif round(ARI) == 9:
            ARIAge = 15
        elif round(ARI) == 10:
            ARIAge = 16
        elif round(ARI) == 11:
            ARIAge = 17
        elif round(ARI) == 12:
            ARIAge = 18
        elif round(ARI) >= 13:
            ARIAge = 24
        print('Automated Readability Index : ' + str(round(ARI,2)) + ' (about ' + str(ARIAge) + ' year olds).')
        CountA = CountA + 1
    elif Approach[CountA] == '2':
        FKGL = 11.8*(Syllables/Words) + 0.39*(Words/Sentences) - 15.59
        if round(FKGL) <= 1:
            FKGLAge = 7;
        elif round(FKGL) == 2:
            FKGLAge = 8
        elif round(FKGL) == 3:
            FKGLAge = 9
        elif round(FKGL) == 4:
            FKGLAge = 10
        elif round(FKGL) == 5:
            FKGLAge = 11
        elif round(FKGL) == 6:
            FKGLAge = 12
        elif round(FKGL) == 7:
            FKGLAge = 13
        elif round(FKGL) == 8:
            FKGLAge = 14
        elif round(FKGL) == 9:
            FKGLAge = 15
        elif round(FKGL) == 10:
            FKGLAge = 16
        elif round(FKGL) == 11:
            FKGLAge = 17
        elif round(FKGL) >= 12:
            FKGLAge = 18
        print('Flesch-Kincaid Readability Tests : ' + str(round(FKGL,2)) + ' (about ' + str(FKGLAge) + ' year olds).')
        CountA = CountA + 1
    elif Approach[CountA] == '3':
        # Can't find table which use for compare with age
        SMOG = math.sqrt(float(Polysyllables)*30/float(Sentences))*1.0430  +3.1291
        if round(SMOG) <= 1:
            SMOGAge = 6;
        elif round(SMOG) == 2:
            SMOGAge = 7
        elif round(SMOG) == 3:
            SMOGAge = 9
        elif round(SMOG) == 4:
            SMOGAge = 10
        elif round(SMOG) == 5:
            SMOGAge = 11
        elif round(SMOG) == 6:
            SMOGAge = 12
        elif round(SMOG) == 7:
            SMOGAge = 13
        elif round(SMOG) == 8:
            SMOGAge = 14
        elif round(SMOG) == 9:
            SMOGAge = 15
        elif round(SMOG) == 10:
            SMOGAge = 16
        elif round(SMOG) == 11:
            SMOGAge = 17
        elif round(SMOG) == 12:
            SMOGAge = 18
        elif round(SMOG) >= 13:
            SMOGAge = 24
        print('Simple Measure of Gobbledygook : ' + str(round(SMOG,2)) + ' (about ' + str(SMOGAge) + ' year olds).')
        CountA = CountA + 1
    elif Approach[CountA] == '4':
        # Can't find table which use for compare with age
        CLI = math.sqrt(float(Polysyllables)*30/float(Sentences))*1.0430  +3.1291
        if round(CLI) <= 1:
            CLIAge = 6;
        elif round(CLI) == 2:
            CLIAge = 7
        elif round(CLI) == 3:
            CLIAge = 9
        elif round(CLI) == 4:
            CLIAge = 10
        elif round(CLI) == 5:
            CLIAge = 11
        elif round(CLI) == 6:
            CLIAge = 12
        elif round(CLI) == 7:
            CLIAge = 13
        elif round(CLI) == 8:
            CLIAge = 14
        elif round(CLI) == 9:
            CLIAge = 15
        elif round(CLI) == 10:
            CLIAge = 16
        elif round(CLI) == 11:
            CLIAge = 17
        elif round(CLI) == 12:
            CLIAge = 18
        elif round(CLI) >= 13:
            CLIAge = 24
        print('Coleman-Liau Readability Index : ' + str(round(CLI,2)) + ' (about ' + str(CLIAge) + ' year olds).')
        CountA = CountA + 1
AverageAge = (ARIAge + FKGLAge + SMOGAge + CLIAge) / len(Approach)
print('\nThis text should be understood in average by ' + str(round(AverageAge,2)) + ' year olds.')
