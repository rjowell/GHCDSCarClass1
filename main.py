
class Car:

  # Constructor Method
  def __init__(self,_colorInput,fuelType,_tireSize,_hasSpoilers,isConvertible):
    self.color = _colorInput
    self.fuelType = fuelType
    self.tireSize = _tireSize
    self.spoilers = _hasSpoilers
    self.convertible = isConvertible
    self.numOfTires = 4
    self.maxFuel = 30
    self.currentFuel = 15



WyattsCar = Car("Green","Electric",272,True,False)
LeosCar = Car("Blue","Diesel",2,False,True)

print(WyattsCar.tireSize)
print(LeosCar.color)
    



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