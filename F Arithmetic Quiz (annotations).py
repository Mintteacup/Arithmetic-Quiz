import random #Makes random a useable function

def Test(): #Defines test
    name=input("What is your name: ") #Ask the user their name
    print("Hello there",name,"!") #Prints a greeting and name
    input(" ") #prints a blank line
    print("I will be asking you 10 simple arithmetic questions, enjoy!") # prints a sentence

    finish = False #Sets finish as false
    questions = 0 #Sets the value of questions
    correct = 0 #Sets the value of correct

    while finish == False: #While finish is false do something
        choice = random.choice("+-x") #sets the value of choice to a random choice
        if questions < 10: #Checks if questions is less than 10
            number1 = random.randrange(1,10) #sets he value of number1 to be a random number
            number2 = random.randrange(1,10) #sets he value of number2 to be a random number
            print((number1),(choice),(number2)) #prints the values number1, choice and number2
            answer=int(input("What is the answer? ")) #Asks the user what the answer is and makes sure it is a int
            questions = questions + 1 #Adds 1 to questions' value

            if choice==("+"): #checks if choice is addition
                answer_ = number1+number2 #sets answer_ to number1+number2
                if answer==answer_: #checks if the answer is the same as answer_
                    print("That's the correct answer") #Prints a sentence
                    correct = correct + 1 #Adds 1 to correct's value
                else:
                    print("Wrong answer, the answer was",answer_,"!") #prints a sentence and answer_

            if choice==("x"): #Checks if choice is multiplication
                answer_ = number1*number2 #sets answer_ to number1*number2
                if answer==answer_: #checks if the answer is the same as answer_
                    print("That's the correct answer") #prints a sentence
                    correct = correct + 1 #adds 1 to correct
                else:
                    print("Wrong answer, the answer was",answer_,"!") #prints a sentence and answer_

            if choice==("-"): #checks if choice is subtraction
                answer_ = number1-number2 #sets answer_ to number1-number2
                if answer==answer_: #checks if the answer is the same as answer_
                    print("That's the correct answer") #prints a sentence
                    correct = correct + 1 #adds 1 to correct
                else:
                    print("Wrong answer, the answer was",answer_,"!") #prints a sentence and asnwer_
        else:
            finish = True #Sets finish as true
    else:
            print("Good job",name,"! You have finished the quiz") #prints a sentence and name
            print("You scored " + str(correct) + "/10 questions.") #prints a sentence and how many you got correct (correct)

Test() #tells the program to go back to Test
