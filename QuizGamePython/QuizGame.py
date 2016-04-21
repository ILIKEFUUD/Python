"""
Rahul Shah
Pd 6
QuizGame.py
Quiz game about the history of technology
"""

#variables
answers=[]
qNum = 0 #question number
score = 0 #player's score
#read in answerKey.txt and store in answers list
with open("answerKey.txt", "r") as answerKey:
    for a in answerKey:
        answers.append(a)
#read in questions file
with open("questions.txt", "r") as questions:
    
    for i in questions:#check every line
        if(qNum <= 10):#makes sure runs all 10 questions
            if("%" not in i): #stops at every % to seperate questions
                print(i)
            else:
                answ = input("What is your answer: ")#if theres a % then ask for input
                if(int(answers[qNum]) == int(answ)):
                    score+=1 #if they're right increase score
                qNum+=1#increase question number
#output score in percentage
print("Your score is: " + str(100 * (score/10)) + "%")
        
    
    
