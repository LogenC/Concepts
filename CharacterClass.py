"""
This is a very introductory example case where you use a Class to create characters that can move and fight
  Obviously more methods can be added on to this making use of the 2-D coordinates or the intelligence, feel free to reuse this code
  and make yourself familiar with classes and add more functionality
  It is not very dynamic, and isn't suppose to be as this is more instructional and for reference
Strength, Speed, and Intelligence are random-ized between the interval [1,3]
    I use r.randint(1,4) because the 4 (end value) is not included
"""

import random as r

class Character:

    #health = 10
    def __init__(self, name="",Ycor = 0,Xcor = 0, strength= r.randint(1,4), speed= r.randint(1,4), intelligence= r.randint(1,4)):
        #self.health = health
        self.name = name
        self.Xcor = Xcor
        self.Ycor = Ycor
        self.strength = int(strength)
        self.speed = int(speed)
        self.intelligence = int(intelligence)
        if self.strength + self.speed + self.intelligence > 10:
            self.strength = 1
            self.speed = 1
            self.intelligence = 1

    def move(self, dir):
        if dir == "u":
            self.y += self.speed
        elif dir =="d":
            self.y -= self.speed
        elif dir == "l":
            self.x -= self.speed
        elif dir == "r":
            self.x += self.speed

    def fight(self, opp):
        block = r.randrange(3)
        if self.strength + block > opp.strength:
            return str(self.name) + " is the winner"
        else:
            return str(opp.name) + " is the winner"

Bo = Character("Bo")
LeRoy = Character("LeRoy")

print(Bo.fight(LeRoy))
