from carFile import Car
from dogFile import Dog
from person import Person
# def __init__(self,_name,_height,_hairColor,_eyeColor,_skinColor):

Thomas = Person("Thomas",74,"Dark Brown","Purple","Green")


Jayqueun = Person("Jayqueun",70,"Black","Brown","Blue")

Jayqueun.eat(50)
Jayqueun.eat(10)


DevonsDog = Dog("Golden","Small",True,"F","Golden Retriever")
WyattsCar = Car("Green","Electric",272,True,False)
LeosCar = Car("Blue","Diesel",2,False,True)

WyattsCar.drive()
WyattsCar.explode()
    



'''
OBJECT-ORIENTED PROGRAMMING

WHAT DO YOU NEED TO BUILD A CAR?
-Factory
-Engine
-Body
-Tires
-Glass
-Interior Material
-Turbo
-Fuel Source: Gas / Electric / Diesel

HOW CAN YOU CUSTOMIZE A CAR?
-Paint color
-Spoliers
-Tires - 4
-Shatter the windows
-Take off doors
-Hood Ornament
-Air Freshener
-Convertible
-Nitro
-Remove Springs frmo tires

WHAT CAN A CAR DO?
-Drive - Forward/Backward
-Turn - Left/Right
-Crash
-Brake
-Park - Self-Park
-Neutral
-Run over stuff
-turn on blinkers

'''






'''
def numLetters(name):
  return len(name)

def classSorting(name):
  if numLetters(name) <= 4:
    print(name +" ,You are in class A")
  else:
    print(name +", You are in class B")

classSorting(input("What is your name?"))
'''



'''
def numLettersInName():
  name_input = input("Enter Your Name: ")
  numLetters = len(name_input) # Integer
  print("Your name has "+str(numLetters)+" letters")



def sayGoodMorning(name):
  print("Good Morning "+name+", how are you")

sayGoodMorning("Devon")
sayGoodMorning("Peyton")
sayGoodMorning("Croix")
sayGoodMorning("Mr. Russ")
'''