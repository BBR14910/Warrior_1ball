import random


class Warrior:
    def __init__(self):
        self.first_warrior_hp = 100
        self.first_warrior_attack = 20
        self.second_warrior_hp = 100
        self.second_warrior_attack = 20
        self.chose = random.randint(1, 3)

    def first_warrior(self):
        self.second_warrior_hp -= self.first_warrior_attack
        if self.second_warrior_hp > 0:
            print("Первый воин атакует. У второго воина осталось = ",
                  self.second_warrior_hp, " здоровья", sep='')
            self.start_battle()
        else:
            print("Первый воин победил!")

    def second_warrior(self):

        self.first_warrior_hp -= self.second_warrior_attack
        if self.first_warrior_hp > 0:
            print("Второй воин атакует. У первого воина осталось = ",
                  self.first_warrior_hp, " здоровья", sep='')
            self.start_battle()

        else:
            print("Второй воин победил!")

    def start_battle(self):

        self.chose = random.randint(1, 3)

        if self.chose == 1:
            self.first_warrior()

        else:
            self.second_warrior()


battle = Warrior()
battle.start_battle()
