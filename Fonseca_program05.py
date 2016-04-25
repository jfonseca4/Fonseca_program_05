#jordan Fonseca
#program 5


#treasure Class 2.1



class treasure(object):  #treasure parent class

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def getType(self):  #type of treasure
        return self.type

    def getValue(self):  #value of treasure, whether nutrition, attack, defense, or currency
        return self.value
        


class food(treasure): #food sub class


    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.isPickup = False #to start it isnt picked up, so false
        self.isEat = False #not eaten yet

    def getType(self):
        return "food"

    def getValue(self):  #nutrition value of food is 5
        return 5

    def pickup(self):
        self.ispickup = True  #when picked up it is true

    def eat(self): #when eaten
        self.isEat = True

class armor(treasure):  #armor sub class

    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.isWorn = False #to start, wearing armor is false

    def getType(self):
        return "armor"

    def getValue(self): #defense level of armor is 10
        return 10

    def wear(self):
        self.isWorn = True  #if armor is worn

    def remove(self):  #to take off armor
        self.isWorn = False

        return self.isWorn == getWorn  #returns the value of the worn armor

class gold(treasure): #gold sub class

    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.isPickup = False

    def getType(self):
        return "gold"

    def getValue(self):  #gold is worth 100
        return 100

    def pickup(self):
        self.ispickup = True #when gold is picked up

class weapon(treasure):  #weapon sub class

    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.iswield = False

    def getType(self):
        return "weapon"

    def getValue(self): #attack level is 50 
        return 50

    def wield(self):
        self.iswield = True #if weapon is wielded

    def unwield(self):  #when weapon is unwielded 
        self.isWield = False

        return self.isWield == getWield


#player class 2.2

class player():  #player class

    def __init__(self, name, exp, hp):
        self.name = name  #name of player
        self.exp = exp  #experience level
        self.hp = hp  #health level of player
        self.islook_at = False #player is not looking at anything
        self.isequip = False #player has not equiped anything
        self.iswield = False #soemthing is not wielded
        self.isEat = False #not eaten yet

    def is_alive(self):
        return self.hp > 0  #makes sure player is alive

    def islook_at(self):
        self.islook_at = True #when player looks at something

    def isequip(self):
        self.isequip = True #when player has something equiped

    def wield(self):
        self.iswield = True #if something is wielded

    def unwield(self):  #when something is unwielded 
        self.isWield = False

        return self.isWield == getWield

    def eat(self): #when eaten
        self.isEat = True
    

#3.1.1     

#project 1

height = 15 #height of grid will be 15

for k in range(0, height + 1):
    if(k == 0) or (k == height):
        print('#' * height)
    else:
        print('#' + ' ' * (height  -2) + '#')

#i was not able to figure out how to generate the length of the grid so i
#only included the height. 

#Also, i could not figure out how to generate the multiple characters inside the grid.


#4.1-

class Action():   #creating an action class for player movements
    def __init__(self, method, name, key):
        self.method = method
        self.name = name
        self.key = key

    def __str__(self):
        return "{}: {}". format(self.key, self.name)


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=player.move_west, name= 'move west',key='h') #when using h, player moves west.

class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=player.move_south, name= 'move south',key='j') #when using j, player moves south.


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=player.move_north, name= 'move north',key='k') #when using k, player moves north.

class MoveEast(Action):
    def __init__(self):
        super().__init__(method=player.move_east, name= 'move east',key='l') #when using l, player moves east.

class MoveUpStairs(Action):
    def __init__(self):
        super().__init__(method=player.move_upStairs, name= 'move up stairs',key='^') #when using ^, player moves up stairs.

class MoveDownStairs(Action):
    def __init__(self):
        super().__init__(method=player.move_downStairs, name= 'move down stairs',key='v') #when using v, player moves down stairs.


