import random


# question 1
def question1():
    print("\nWhich of the following is not a real US town name?\n")
    print("A: Burnt Porcupine   B: Ding Dong   C: Rock Bottom\n")


# question 2
def question2():
    print("\nWhich of these dog breeds rank the lowest in intelligence?\n")
    print("A: Chow chow   B: Corgi   C: Poodle\n")


# question 3
def question3():
    print("\nWhat tattoo does Jess have?\n")
    print("A: Cobra   B: Python   C: Viper\n")


# question 4
def question4():
    print("\nSome months have 31 days, some have 31 days. How many months have 28 days?\n")
    print("A: 0   B: 1   C: 12\n")


# question 5
def question5():
    print("\nWhich of the following is not a prime number?\n")
    print("A: 3   B: 5   C: 10\n")


#  defines an app that protects a drunk user from texting his/her ex! *GASP*
def DrunkProtection():

    # introduces what this app does, and prompts user for consent to proceed
    print('\nThis is an app to protect you from sending drunk texts!!! Do you want to continue? [y/n]\n')

    answer = input().upper()

    # if user answers YES, then it proceeds with the following questions
    if answer == "Y":

        # defines a list of the above questions, to be randomly given to user
        myQuestionList = [question1, question2, question3, question4, question5]

        # defines the answer key to the questions defined
        answerDict = {question1: "C", question2: "A", question3: "B", question4: "C", question5: "C"}

        # uses the randomizer to make the user answer between 3 to 5 questions
        x = random.randrange(2,5,1)
        print("\nYou have to answer {} questions to pass this quiz! Press any key to proceed".format(x))

        input()

        # creates an empty list to store user's answers
        answerList = []
        # creates an empty list to store the answers corresponding to the random questions
        answerKey = []

        # Loop
        while x > 0:
            # randomly choose the questions from mySet
            # random.choice(mySet)()
            myQuestionList[x-1]()

            # finds the corresponding answer in the answerDict dictionary, and stores it into the empty answerKey list
            y = myQuestionList[x-1]
            z = answerDict[y]
            answerKey.append(z)

            # stores user input into the empty answerList
            answer = input().upper()
            answerList.append(answer)

            x = x - 1

        # checks if answerList is equal to the answerKey
        if answerList == answerKey:
            # response if user is able to get all answers correct
            print("\nI guess you are sober enough to deal with the consequences of your actions...\n")
        else:
            # response if user fails the quiz
            print("\nLeave your phone alone, go to bed, and thank me tomorrow for stopping you from sending any stupid texts!\n")

    # response if user does not consent to partaking in this quiz
    else:
        print("\nI guess you are sober enough to deal with the consequences of your actions...\n")



DrunkProtection()
