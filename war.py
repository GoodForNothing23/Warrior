#Branch Test
#Test merge
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
        self.quantity += n
        for i in range(n):
            self.army.extend([s()])

    
    @property
    def is_full(self):
        if self.quantity == 0:
            return False
        else:
            return True


class Battle:
    def fight(self, army_1, army_2):
        while army_1.is_full and army_2.is_full:            
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
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
    if unit_1.is_alive:
        return True
    else:
        return False 
  


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    print("Test branch")
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


