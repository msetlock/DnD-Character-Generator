# DnD 5e character generator


class player():
    def __init__(self, char_class, char_race, level, strength, dexterity, intelligence, wisdom, charisma, constitution):
        self.char_class = char_class
        self.char_race = char_race
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.constitution = constitution
        self.name = ''

    def setName(self):
        self.name = input("what is your Name? ")

    def setLevel(self):
        self.level = input("what level are you? ")

    def displayClass(self):
        print(self.char_class)

    def displayRace(self):
        print(self.char_race)

    def displayLevel(self):
        print(self.level)

    def displayStrength(self):
        print(self.strength)

    def displayDex(self):
        print(self.dexterity)

    def displayInt(self):
        print(self.intelligence)

    def displayWis(self):
        print(self.wisdom)

    def displayCharisma(self):
        print(self.charisma)

    def displayCharisma(self):
        print(self.constitution)

    def rundown(self):
        prof = 0
        AS = 0
        if int(self.level) < 5:
            prof = 2
            if int(self.level)==4:
                AS=1
            
        if int(self.level) > 4 and int(self.level) <=8:
            prof = 3
            AS = 1
            if int(self.level)==8:
                AS=2
            
        if int(self.level) > 8 and int(self.level) <= 12:
            prof = 4
            AS = 2
            if int(self.level)==12:
                AS=3

            
        if int(self.level) > 12 and int(self.level) <= 16:
            prof = 5
            AS = 3
            if int(self.level)==16:
                AS=4
            
        if int(self.level) > 16:
            prof = 6
            AS = 4
            if int(self.level)==19:
                AS=5
            

        print('\nYou are ' + self.name + ', a level ' + str(self.level) + ' ' + self.char_race + ' ' + self.char_class + '. Your stats are as follows:\n'
              + 'Strength: ' + str(self.strength) + ' \n'
              'Dexterity: ' + str(self.dexterity) + ' \n'
              'Intelligence: ' + str(self.intelligence) + ' \n'
              'Wisdom: ' + str(self.wisdom) + ' \n'
              'Charisma: ' + str(self.charisma) + ' \n'
              'Constitution: ' + str(self.constitution) + ' \n\n'
              'Your proficiency Bonus is ' + str(prof) +
              '\nYou have ' + str(AS) + ' ability score improvements to spend\n')
