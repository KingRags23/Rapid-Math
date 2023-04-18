import turtle as trtl #importing the turtle library
import random #importing the random library


#creating various global variables to be used throughout the whole code, so that the code recognizes it even when they are used within various loops:

global easyreset
global mediumreset
global hardreset
global difficulty
global easy
global medium
global hard


#SET-UP

wn = trtl.Screen() #creating turtle screen
painter = trtl.Turtle() #creating the turtle called painter
painter.hideturtle() #hiding the turtle on screen


#creating a function below that enables me to move the turtle to wherever I want on the screen without having to say painter.penup() or painter.pendown() or painter.goto() everytime. This made the coding process way easier by directing the turtle to move to specific coordinates all in one line. 

def move(x,y):
  painter.penup()
  painter.goto(x,y)
  painter.pendown()


#WELCOME PAGE

wn.bgcolor("black") #setting screen background color to black
move(-250,0) 
painter.pencolor("red") #setting turtle writing color to red
painter.write("Welcome To Rapid Math", font=("Arial", 30)) #writing the introduction message
painter.pencolor("white") #setting turtle writing color to white
move(-100,-100)
painter.write("Click On Screen For Instructions", font=("Arial",10)) #writing the prompting message so user clicks anywhere on the screen


#INSTRUCTIONS PAGE

#creating a function that is responsible for displaying the instructions page of the game. It tells the user exactly how the game works and allows them to select the level of difficulty.

def instructions(x,y):
  wn.clearscreen() #clears screen
  wn.bgcolor("black") #sets screen color to black
  painter.pencolor("green") #sets turtle writing color to green
  move(-220,100)
  painter.write("You will be given a series of math questions.") #displaying a message that tells user what the game does
  move(-220,0)
  painter.write("Try to get as many problems right. Game stops at the first incorrect answer.") #displaying a message that tells user when the game ends and what the goal is
  move(-220,-100)
  painter.write("Enter 'e' for easy problems, 'm' for medium problems, and 'h' for hard problems.") #directs the user to respond to the prompt on the console by choosing one of the three options


wn.onclick(instructions) #tells the instructions function created above to run if and only if the user clicks on the screen

 
#SELECTING LEVEL OF DIFFICULTY

difficultyvalidcheck = False #creats a boolean to use as placeholder for initial run

#creating values for each level and setting them to the default value of true, and these values will be changed according to what level of difficulty the user selects.
easy = True 
medium = True
Hard = True

while difficultyvalidcheck == False: #creating a condition
  difficulty = input("Choose the difficulty of the problems: 'e' for easy, 'm' for medium and 'h' for hard:") #prompt that asks the user to select from three options
  if difficulty == 'e' or difficulty == 'm' or difficulty == 'h': #checking to make sure that what the user enters is actually one of the three options and not something else
    difficultyvalidcheck = True #ensuring that the loop does not have to run if the user selects one of three right options
    
    if difficulty == 'e': #condition for if the user selects the easy level
      easy = True 
      medium = False
      hard = False
      
    elif difficulty == 'm': #condition for if the user selects the medium level
      easy = False
      medium = True
      hard = False
      
    elif difficulty == 'h': #condition for if the user selects the hard level
      easy = False
      medium = False
      hard = True
  
  elif difficulty != 'e' or difficulty != 'm' or difficulty != 'h': #condition in case the user enters something other than the three options, brings them back to the same loop
    print("You have entered an invalid character. Please enter either 'e', 'm' or 'h'.") #message that indicates to the user that they have not selected one of the three displayed options
    difficultyvalidcheck = False #sets the value to False, which takes it back into the loop

#CREATING FUNCTION FOR RESTARTING GAME IF USER WANTS

def restart(x,y):

  #displaying instructions again
  wn.clearscreen() 
  wn.bgcolor("black")
  painter.pencolor("green") 
  move(-220,100)
  painter.write("You will be given a series of math questions.") 
  move(-220,0)
  painter.write("Try to get as many problems right. Game stops at the first incorrect answer.") 
  move(-220,-100)
  painter.write("Enter 'e' for easy problems, 'm' for medium problems, and 'h' for hard problems.") 

  difficultyvalidcheck = False 

  easy = True 
  medium = True
  hard = True

  #exact same code as above where user selects level of difficulty
  while difficultyvalidcheck == False: 
    difficulty = input("Choose the difficulty of the problems: 'e' for easy, 'm' for medium and 'h' for hard:") 
    if difficulty == 'e' or difficulty == 'm' or difficulty == 'h': 
      difficultyvalidcheck = True 
      if difficulty == 'e': 
        easy = True 
        medium = False
        hard = False
      
      elif difficulty == 'm': 
        easy = False
        medium = True
        hard = False
      
      elif difficulty == 'h': 
        easy = False
        medium = False
        hard = True
  
    elif difficulty != 'e' or difficulty != 'm' or difficulty != 'h': 
      print("You have entered an invalid character. Please enter either 'e', 'm' or 'h'.") 
      difficultyvalidcheck = False 

  if difficulty == 'e': #if the user chose the easy level:
    easygame(easynum1, easynum2, easysign) #call the function that starts the easy level

  if difficulty == 'm': #if the user chose the medium level:
    mediumgame(mediumnum1, mediumnum2, mediumsign) #call the function that starts the medium level

  if difficulty == 'h': #if the user chose the hard level:
    hardgame(hardnum1, hardnum2, hardsign) #call the function that starts the hard level


#CREATING LISTS FOR GAME

#creating the two lists for the easy mode of the game, with each list standing for one respective number in the problem. The sign list contains all the possible arithmetic operators that could be performed on both values. 

easygamelist1 = [1,2,3,4,5,6,7,8,9]
easygamelist2 = [1,2,3,4,5,6,7,8,9]
easygamesigns = ['+','-','*']

#creating the two lists for the medium mode of the game, with each list standing for one respective number. The sign list contains all the possible arithmetic operators that could be performed on both values. Since it is of a higher level, there are greater numbers and one additional sign, which is division. 

mediumgamelist1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
mediumgamelist2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
mediumgamesigns = ['+','-','*','/']

#creating the two lists for the medium mode of the game, with each list standing for one respective number. Since this is the hardest level, it contains numbers from 1-100, which is put into the two lists by the for loop below. Furthermore, there are two additional arithmetic operators in this mode: the modulus and the power operators, which can get pretty challenging at times. 

hardgamelist1 = []
hardgamelist2 = []

i = 0
#a for loop that adds the numbers from 1-100 in both lists for the hard mode
for i in range(101):
  hardgamelist1.append(int(i))
  hardgamelist2.append(int(i))
  i += 1

hardgamelist1.remove(0) #removing zero to prevent division by zero error
hardgamelist2.remove(0) #removing zero to prevent division by zero error

hardgamesigns = ['+','-','*','/','%']


#CREATING THE FUNCTIONS OF THE GAME: ONE FOR EACH LEVEL OF DIFFICULTY

def easygame(x,y,s): 
  easyreset = False #game loop condition: that is, game keeps running as this condition is met
  while easyreset == False:
    #everytime the user gets the right answer, the numbers the operator are randomly generated
    x = random.choice(easygamelist1)
    y = random.choice(easygamelist2)
    s = random.choice(easygamesigns)
    print(x, s, y) #the problem is printed onto the console
    easyanswer = int(input("Answer: ")) #saving the user reponse to the question
    if s == '+':
      if easyanswer == x + y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
        print("Correct!")
        print("---------------------------------------------")
        wn.clearscreen()
        wn.bgcolor("black")
        painter.pencolor("green")
        move(-160,-50)
        painter.write("CORRECT!", font=("Arial",50))
        x = random.choice(easygamelist1)
        y = random.choice(easygamelist2)
        s = random.choice(easygamesigns)
        easyreset = False
      elif easyanswer != x + y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
        print("Incorrect!")
        wn.clearscreen()
        wn.bgcolor("black")
        painter.pencolor("red")
        move(-175,0)
        painter.write("YOU LOSE!", font=("Arial",50))
        easyreset = True
        painter.pencolor("white")
        move(-70,-100)
        painter.write("Click Anywhere To Play Again")
        wn.onclick(restart)
    elif s == '-':
      if easyanswer == x - y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
        print("Correct!")
        print("---------------------------------------------")
        wn.clearscreen()
        wn.bgcolor("black")
        painter.pencolor("green")
        move(-160,-50)
        painter.write("CORRECT!", font=("Arial",50))
        x = random.choice(easygamelist1)
        y = random.choice(easygamelist2)
        s = random.choice(easygamesigns)
        easyreset = False
      elif easyanswer != x - y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
        print("Incorrect!")
        wn.clearscreen()
        wn.bgcolor("black")
        painter.pencolor("red")
        move(-175,0)
        painter.write("YOU LOSE!", font=("Arial",50))
        easyreset = True
        painter.pencolor("white")
        move(-70,-100)
        painter.write("Click Anywhere To Play Again")
        wn.onclick(restart)
    elif s == "*":
      if easyanswer == x * y:#  to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
        print("Correct!")
        print("---------------------------------------------")
        wn.clearscreen()
        wn.bgcolor("black")
        painter.pencolor("green")
        move(-160,-50)
        painter.write("CORRECT!", font=("Arial",50))
        x = random.choice(easygamelist1)
        y = random.choice(easygamelist2)
        s = random.choice(easygamesigns)
        easyreset = False
      elif easyanswer != x * y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
        wn.clearscreen()
        wn.bgcolor("black")
        painter.pencolor("red")
        move(-175,0)
        painter.write("YOU LOSE!", font=("Arial",50))
        easyreset = True
        painter.pencolor("white")
        move(-70,-100)
        painter.write("Click Anywhere To Play Again")
        wn.onclick(restart)

#assigning values to three variables that serve as a parameters of the function later on
easynum1 = random.choice(easygamelist1)
easynum2 = random.choice(easygamelist2)
easysign = random.choice(easygamesigns)      
      

def mediumgame(x,y,s):
  mediumreset = False #game loop condition: that is, game keeps running as this condition is met
  while mediumreset == False: #everytime the user gets the right answer, the numbers the operator are randomly generated
    mediumgamesigns = ['+','-','*','/']
    x = random.choice(mediumgamelist1)
    y = random.choice(mediumgamelist2)
    s = random.choice(mediumgamesigns)
    if x % y == 0: #if the division operator yields in a decimal value, remove the division operator from the sign list since we want only integer answers
      mediumgamesigns = ['+','-','*','/']
      s = random.choice(mediumgamesigns) #regenerating the sign
      print(x,s,y) #the problem is printed onto the console
      mediumanswer = int(input("Answer: ")) #saving the user reponse to the question
      if s == '+':
        if mediumanswer == x + y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(mediumgamelist1)
          y = random.choice(mediumgamelist2)
          s = random.choice(mediumgamesigns)
          mediumreset = False
        elif mediumanswer != x + y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-175,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          mediumreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == '-':
        if mediumanswer == x - y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(mediumgamelist1)
          y = random.choice(mediumgamelist2)
          s = random.choice(mediumgamesigns)
          mediumreset = False
        elif mediumanswer != x - y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-175,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          mediumreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == "*":
        if mediumanswer == x * y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(mediumgamelist1)
          y = random.choice(mediumgamelist2)
          s = random.choice(mediumgamesigns)
          mediumreset = False
        elif mediumanswer != x * y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-175,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          mediumreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == '/':
        if mediumanswer == x / y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(mediumgamelist1)
          y = random.choice(mediumgamelist2)
          s = random.choice(mediumgamesigns)
          mediumreset = False
        elif mediumanswer != x / y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-175,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          mediumreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
    elif x % y != 0: #condition that checks whether or not division yields in an integer value; if not, the sign is regenerated to anything other than a division operator
      mediumgamesigns = ['+','-','*']
      s = random.choice(mediumgamesigns)
      print(x,s,y)
      mediumanswer = int(input("Answer:"))
      if s == '+':
        if mediumanswer == x + y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(mediumgamelist1)
          y = random.choice(mediumgamelist2)
          s = random.choice(mediumgamesigns)
          mediumreset = False
        elif mediumanswer != x + y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-175,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          mediumreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == '-':
        if mediumanswer == x - y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(mediumgamelist1)
          y = random.choice(mediumgamelist2)
          s = random.choice(mediumgamesigns)
          mediumreset = False
        elif mediumanswer != x - y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-175,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          mediumreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == "*":
        if mediumanswer == x * y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(mediumgamelist1)
          y = random.choice(mediumgamelist2)
          s = random.choice(mediumgamesigns)
          mediumreset = False
        elif mediumanswer != x * y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-175,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          mediumreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)

#assigning values to three variables that serve as a parameters of the function later on
mediumnum1 = random.choice(mediumgamelist1)
mediumnum2 = random.choice(mediumgamelist2)
mediumsign = random.choice(mediumgamesigns)      
      
    

def hardgame(x,y,s):
  hardreset = False #game loop condition: that is, game keeps running as this condition is met
  while hardreset == False: #everytime the user gets the right answer, the numbers the operator are randomly generated
    hardgamesigns = ['+','-','*','/','%']
    x = random.choice(hardgamelist1)
    y = random.choice(hardgamelist2)
    s = random.choice(hardgamesigns)
    if x % y == 0: #if the division operator yields in a decimal value, remove the division operator from the sign list since we want only integer answers
      hardgamesigns = ['+','-','*','/','%']
      s = random.choice(hardgamesigns)
      print(x,s,y) #the problem is printed onto the console
      hardanswer = int(input("Answer: ")) #saving the user reponse to the question
      if s == '+':
        if hardanswer == x + y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(hardgamelist1)
          y = random.choice(hardgamelist2)
          s = random.choice(hardgamesigns)
          hardreset = False
        elif hardanswer != x + y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-170,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          hardreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == '-':
        if hardanswer == x - y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(hardgamelist1)
          y = random.choice(hardgamelist2)
          s = random.choice(hardgamesigns)
          hardreset = False
        elif hardanswer != x - y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-170,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          hardreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == "*":
        if hardanswer == x * y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(hardgamelist1)
          y = random.choice(hardgamelist2)
          s = random.choice(hardgamesigns)
          hardreset = False
        elif hardanswer != x * y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-170,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          hardreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == '/':
        if hardanswer == x / y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(hardgamelist1)
          y = random.choice(hardgamelist2)
          s = random.choice(hardgamesigns)
          hardreset = False
        elif hardanswer != x / y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-170,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          hardreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == '%': 
        if hardanswer == x % y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(hardgamelist1)
          y = random.choice(hardgamelist2)
          s = random.choice(hardgamesigns)
          hardreset = False
        elif hardanswer != x % y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-170,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          hardreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
    elif x % y != 0: #condition that checks whether or not division yields in an integer value; if not, the sign is regenerated to anything other than a division operator
      hardgamesigns = ['+','-','*','%']
      s = random.choice(hardgamesigns)
      print(x,s,y)
      hardanswer = int(input("Answer:"))
      if s == '+':
        if hardanswer == x + y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(hardgamelist1)
          y = random.choice(hardgamelist2)
          s = random.choice(hardgamesigns)
          hardreset = False
        elif hardanswer != x + y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-170,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          hardreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == '-':
        if hardanswer == x - y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(hardgamelist1)
          y = random.choice(hardgamelist2)
          s = random.choice(hardgamesigns)
          hardreset = False
        elif hardanswer != x - y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-170,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          hardreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == "*":
        if hardanswer == x * y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen() 
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(hardgamelist1)
          y = random.choice(hardgamelist2)
          s = random.choice(hardgamesigns)
          hardreset = False
        elif hardanswer != x * y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-170,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          hardreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
      elif s == '%':
        if hardanswer == x % y: #checking to see if the user's response is equal to the actual answer. If it is, "CORRECT" is displayed on the screen and it moves on to the next problem.
          print("Correct!")
          print("-------------------------------------------")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("green")
          move(-160,-50)
          painter.write("CORRECT!", font=("Arial",50))
          x = random.choice(hardgamelist1)
          y = random.choice(hardgamelist2)
          s = random.choice(hardgamesigns)
          hardreset = False
        elif hardanswer != x % y: #condition that if the user's input is not equal to the actual answer, the game ends and the message "YOU LOSE" is displayed.
          print("Incorrect!")
          wn.clearscreen()
          wn.bgcolor("black")
          painter.pencolor("red")
          move(-170,0)
          painter.write("YOU LOSE!", font=("Arial",50))
          hardreset = True
          painter.pencolor("white")
          move(-70,-100)
          painter.write("Click Anywhere To Play Again")
          wn.onclick(restart)
          
      
#assigning values to three variables that serve as a parameters of the function later on
hardnum1 = random.choice(hardgamelist1)
hardnum2 = random.choice(hardgamelist2)
hardsign = random.choice(hardgamesigns)      
            
            
  
#checking to see the difficulty of the game that the user chose, and chooses the appriopriate level by calling the respective function  

if difficulty == 'e': #if the user chose the easy level:
  easygame(easynum1, easynum2, easysign) #call the function that starts the easy level

if difficulty == 'm': #if the user chose the medium level:
  mediumgame(mediumnum1, mediumnum2, mediumsign) #call the function that starts the medium level

if difficulty == 'h': #if the user chose the hard level:
  hardgame(hardnum1, hardnum2, hardsign) #call the function that starts the hard level


wn.mainloop() 

