from random import randint
import pickle
def RndmLeet():
    newProblem = input("Enter the problem you've done today:")
    newLink = input("enter the link of the new problem:")

    with open('problems.pkl', 'ab') as file:
        pickle.dump((newProblem,newLink), file)

    with open('problems.pkl', 'rb') as file:
        problems = []
        while True:
            try:
                item = pickle.load(file)
                problems.append(item)
            except EOFError:
                break
    
    try:
        rndmProblem = randint(0,len(problems) - 2)
        print(problems[rndmProblem])
    
    except: 
        print("this is your first problem, nothing to review for today!")
   

RndmLeet()




