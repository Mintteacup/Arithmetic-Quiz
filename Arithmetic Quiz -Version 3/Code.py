file = open

def menu():
    entry = False
    while entry == False:
        print('            ***************************')
        print('            * Arithmetic Quiz Scores! *')
        print('            ***************************')
        print('')
        print('')
        print('1. Alphabetic Order (Highest)')
        print('')
        print('2. Highest - Lowest')
        print('')
        print('3. Average (Highest-Lowest)')
        print('')
        print('4. Quit')
        print('')
        choice=input('What do you want to do - 1, 2, 3, 4? ')
        if choice == '1':
            print("")
            alphabetic_order()
            entry = False
        elif choice == '2':
            print("")
            highest_lowest()
            entry = False
        elif choice == '3':
            print("")
            average()
            entry = False
        elif choice == '4':
            print("Goodbye")
            entry = True
        else:
            print("")
            print("I'm Sorry But That Is Not An Option, Please Choose Again!")
            input("Press Enter!")
            print("")

def alphabetic_order():
    inputFile = open("Names.txt", 'r')
    lineList = inputFile.readlines()
    lineList.sort()
    for line in lineList:
        line = line.strip()
        parts = line.split(" - ")
        name =   parts[0]
        score1 = parts[1]
        score2 = parts[2]
        score3 = parts[3]
        alphabetical=(max(score1, score2, score3))
        print(" "+ name + "   " + alphabetical)
        print("")
    inputFile.close()

def highest_lowest():
    inputFile = open("Names.txt", 'r')
    lineList = inputFile.readlines()
    lineList.sort()
    for line in lineList:
        line = line.strip()
        parts = line.split(" - ")
        name =   parts[0]
        score1 = int(parts[1])
        score2 = int(parts[2])
        score3 = int(parts[3])
        total=(score1, score2, score3)
        highestlowest=sorted(total, key=int, reverse=True)
        print(" "+ name + "  " + str(highestlowest))
        print("")
    inputFile.close()

def average():
    inputFile = open("names.txt", "r")
    lineList = inputFile.readlines()
    lineList.sort()
    for line in lineList:
        line = line.strip()
        parts = line.split(" - ")
        name =   parts[0]
        score1 = parts[1]
        score2 = parts[2]
        score3 = parts[3] 
        total= int(score1) + int(score2) + int(score3)
        average_= int(total) /3
        print (" "+ name + " " + str(round(average_)))
        print("")
    inputFile.close()
    
menu()
