# Taken from mission The Warriors

class Warrior:
    health = 50
    attack = 5
    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    
class Knight(Warrior):
    attack = 7
    

class Army:
    def __init__(self):
        self.quantity = 0
        self.army = list()
    
    def add_units(self, s, n):
        if s == Warrior:
            self.quantity += n
            for i in range(n):
                self.army.extend([Warrior()])
            
        elif s == Knight:
            self.quantity += n
            for i in range(n):
                self.army.extend([Knight()])
        else:
            print("not class Knight or Warrior")
    
    @property
    def is_full(self):
        if self.quantity == 0:
            return False
        else:
            return True


class Battle:
    def fight(self, army_1, army_2):
        while army_1.is_full and army_2.is_full:
            print(army_1.army)
            print(army_2.army)
            print(army_1.army[army_1.quantity-1].health)
            print(army_2.army[army_2.quantity-1].health)
            
            if fight(army_1.army[army_1.quantity-1], army_2.army[army_2.quantity-1]):
                army_2.quantity -= 1
                army_2.army.pop()
            else:
                army_1.quantity -= 1
                army_1.army.pop()
        print(army_1.is_full)    
        if army_1.is_full:
            return True
        else:
            return False
        
            
def fight(unit_1, unit_2):
    j = True
    i = 1
    while (unit_1.health > 0) and (unit_2.health > 0):
        if(i%2):
            unit_2.health -= unit_1.attack
            i += 1
        else:
            unit_1.health -= unit_2.attack
            i += 1
    if(unit_1.health > 0):
        j = True
    else:
        j = False
    return j    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")