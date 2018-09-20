#Branch Test
class Warrior:
    health = 50
    attack = 5
    defense = 0
    vampirism = 0
    lancerism = 0
    num_attack = 0
    
    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
            
    @property
    def is_lancer(self):
        if self.lancerism > 0:
            return False
        else:
            return True
    
class Knight(Warrior):
    attack = 7


class Defender(Warrior):
    health = 60
    attack = 3
    defense = 2
    
class Vampire(Warrior):
    health = 40
    attack = 4
    vampirism = 0.5
    
    
class Lancer(Warrior):
    healt = 50
    attack = 6
    lancerism = 0.5
    num_attack = 0
    

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
            bool = fight(army_1.army[army_1.quantity-1], army_2.army[army_2.quantity-1])
            if bool:
                sum_attack_1 = army_1.army[army_1.quantity-1].attack * army_1.army[army_1.quantity-1].lancerism
                sum_attack_2 = army_2.army[army_2.quantity-1].attack * army_2.army[army_2.quantity-1].lancerism
                power_attack_1 = army_1.army[army_1.quantity-1].attack * army_1.army[army_1.quantity-1].lancerism
                power_attack_2 = army_2.army[army_2.quantity-1].attack * army_2.army[army_2.quantity-1].lancerism
                num_attack_1 = army_1.army[army_1.quantity-1].num_attack
                num_attack_2 = army_2.army[army_2.quantity-1].num_attack
                army_1.army[army_1.quantity-1].num_attack = 0
                army_2.army[army_2.quantity-1].num_attack = 0
                army_2.quantity -= 1
                army_2.army.pop()
                if army_1.quantity > 2:
                    if power_attack_2 > army_1.army[army_1.quantity-1].defense:
                        army_1.army[army_1.quantity-1].health -= (power_attack_2 - army_1.army[army_1.quantity-1].defense) * num_attack_2
                if army_2.quantity > 2:
                    if power_attack_1 > army_2.army[army_2.quantity-1].defense:
                        army_2.army[army_2.quantity-1].health -= (power_attack_1 - army_2.army[army_2.quantity-1].defense) * num_attack_1
            else:
                sum_attack_1 = army_1.army[army_1.quantity-1].attack * army_1.army[army_1.quantity-1].lancerism
                sum_attack_2 = army_2.army[army_2.quantity-1].attack * army_2.army[army_2.quantity-1].lancerism
                power_attack_1 = army_1.army[army_1.quantity-1].attack * army_1.army[army_1.quantity-1].lancerism
                power_attack_2 = army_2.army[army_2.quantity-1].attack * army_2.army[army_2.quantity-1].lancerism
                army_1.army[army_1.quantity-1].num_attack = 0
                army_2.army[army_2.quantity-1].num_attack = 0
                num_attack_1 = army_1.army[army_1.quantity-1].num_attack
                num_attack_2 = army_2.army[army_2.quantity-1].num_attack
                army_1.quantity -= 1
                army_1.army.pop()
                if army_1.quantity > 2:
                    if power_attack_2 > army_1.army[army_1.quantity-1].defense:
                        army_1.army[army_1.quantity-1].health -= (power_attack_2 - army_1.army[army_1.quantity-1].defense) * num_attack_2
                if army_2.quantity > 2:
                    if power_attack_1 > army_2.army[army_2.quantity-1].defense:
                        army_2.army[army_2.quantity-1].health -= (power_attack_1 - army_2.army[army_2.quantity-1].defense) * num_attack_1
             
                  
                        
        if army_1.is_full:
            return True
        else:
            return False
        
            
def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        if unit_1.is_alive and unit_2.is_alive:
            if unit_2.defense < unit_1.attack:
                unit_2.health -= unit_1.attack - unit_2.defense
                unit_1.health += (unit_1.attack - unit_2.defense)*unit_1.vampirism
                if type(unit_1) == Lancer:
                    unit_1.num_attack += 1
            elif unit_1.is_lancer:
                unit_1.num_attack += 1
            if unit_2.is_alive:
                if unit_1.defense < unit_2.attack:
                    unit_1.health -= unit_2.attack - unit_1.defense
                    unit_2.health += (unit_2.attack - unit_1.defense)*unit_2.vampirism
                    if type(unit_1) == Lancer:
                        unit_1.num_attack += 1
                elif unit_1.is_lancer:
                    unit_1.num_attack += 1
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

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #fight tests
    print("WORK!!!")
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #fight tests
    print("WORK!!!")
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
