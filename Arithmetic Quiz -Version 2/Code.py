import random #makes random a useable function
import datetime #makes datetime a useable function
file = open #opens file so we can edit it

def test(): #Defines test
    name=input("What is your first name: ") #Ask the user their name
    sname=input("What is your  surname: ") #Ask the user their surname
    class_=input("What class are you in: ") #Ask the user what class they are in
    print("Hello there",name,"!") #Prints a greeting and name
    print("I will be asking you 10 simple arithmetic questions, enjoy!") # prints a sentence
    input("") #prints a blank line
    
    finish = False #Sets finish as false
    questions = 0 #Sets the value of questions
    correct = 0 #Sets the value of correct

    while finish == False: #While finish is false do something
        choice = random.choice("+-x") #sets the value of choice to a random choice
        if questions < 10: #Checks if questions is less than 10
            number1 = random.randint(1,10) #sets he value of number1 to be a random number
            number2 = random.randint(1,10) #sets he value of number2 to be a random number
            print((number1),(choice),(number2)) #prints the values number1, choice and number2
            answer=int(input("What is the answer? ")) #Asks the user what the answer is and makes sure it is a int
            questions = questions + 1 #Adds 1 to questions' value

            if choice==("+"): #checks if choice is addition
                answer_ = number1+number2 #sets answer_ to number1+number2
                if answer==answer_: #checks if the answer is the same as answer_
                    print("That's the correct answer") #Prints a sentence
                    print(" ") #prints a blank line
                    correct = correct + 1 #Adds 1 to correct
                else:
                    print("Wrong answer, the answer was",answer_,"!") #prints a sentence and answer_
                    print(" ") #prints a blank line

            if choice==("x"): #Checks if choice is multiplication
                answer_ = number1*number2 #sets answer_ to number1*number2
                if answer==answer_: #checks if the answer is the same as answer_
                    print("That's the correct answer") #prints a sentence
                    print(" ") #prints a blank line
                    correct = correct + 1 #adds 1 to correct
                else:
                    print("Wrong answer, the answer was",answer_,"!")
                    print(" ") #prints a blank line

            elif choice==("-"):
                answer_ = number1-number2

                if answer==answer_:
                    print("That's the correct answer") #prints a sentence
                    print(" ") #prints a blank line
                    correct = correct + 1 #adds 1 to correct
                else:
                    print("Wrong answer, the answer was",answer_,"!") #prints a sentence and answer_
                    print(" ") #prints a blank line
        else:
            finish = True #Sets finish as true
    else:
            print("Good job",name,"! You have finished the quiz") #prints a a sentence and name
            print("You scored " + str(correct) + "/10 questions.") #prints a sentence and how many you got correct (correct)
            if correct < 5: #Checks if correct is less than 5
                print("At least you tried") #prints a sentence
            elif correct == 5: #Checks if correct is equal to 5
                print("Well done! You got half of the questions correct!") #prints a sentence
            elif correct > 5: #Checks if correct is more than 5
                print("Well done! You did good!") #prints a sentence

    if class_ == "1": #Checks if class_ is 1
        file = open("Class1.txt", 'a') #creates or opens a file
        file.write(str(datetime.datetime.now()) + " - Name: " + name + " " + sname + " - Class: " + class_ + " - Score: " + str(correct) + "/10 -" +"\n") #writes to a file
        file.close() #closes the file
    if class_ == "2": #Checks if class_ is 2
        file = open("Class2.txt", 'a') #creates or opens a file
        file.write(str(datetime.datetime.now()) + " - Name: " + name + " " + sname + " - Class: " + class_ + " - Score: " + str(correct) + "/10 -" +"\n") #writes to a file
        file.close() #closes the file
    if class_ == "3": #Checks if class_ is 3
        file = open("Class3.txt", 'a') #creates or opens a file
        file.write(str(datetime.datetime.now()) + " - Name: " + name + " " + sname + " - Class: " + class_ + " - Score: " + str(correct) + "/10 -" +"\n") #writes to a file
        file.close() #closes the file

test() #tells the program to go back to test
