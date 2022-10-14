# DnD 5e character generator
import random
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
           'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'Artificer']

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


    def setClass(self):
        self.char_class = random.choice(classes)
    def setName(self):
        self.name = input("what is your Name? ")

    def setLevel(self):
        self.level = input("what level are you? ")

    """ def displayClass(self):
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
        print(self.constitution) """

    def statMod(self, stat):
        mod=0
        if int(stat) == 1:
            mod= -5
        if  2 <=int(stat)>= 3:
            mod= 9
        if  4 <=int(stat)>= 5:
            mod= -3
        if  6 <=int(stat)>= 7:
            mod =-2
        if  8 <=int(stat)>= 9:
            mod= -1
        if  10 <=int(stat)>= 11:
            mod= 0
        if  12 <=int(stat)>= 13:
            mod= 1
        if 14 <=int(stat)>= 15:
            mod= 2 
        if 16 <=int(stat)>= 17:
            mod= 3 
        if 18 <=int(stat)>= 19:
            mod= 4  
        if 20 <=int(stat)>= 21:
            mod= 5
        return mod 
    def determineAP(self):
        prof = 0
        AS = 0
        if int(self.level) < 5:
            prof = 2
            if int(self.level)==4:
                AS=1
            
        if  4 < int(self.level) <=8:
            prof = 3
            AS = 1
            if int(self.level)==8:
                AS=2
            
        if  8 < int(self.level) <= 12:
            prof = 4
            AS = 2
            if int(self.level)==12:
                AS=3

            
        if 12 < int(self.level) <= 16:
            prof = 5
            AS = 3
            if int(self.level)==16:
                AS=4
            
        if int(self.level) > 16:
            prof = 6
            AS = 4
            if int(self.level)==19:
                AS=5
        return prof, AS

    def rundown(self):
        result = self.determineAP()
        prof=result[0]
        AS=result[1]
        if str(self.char_class)== str(classes[4]):
            if int(self.level)>=6:
                AS+=1
                
                if int(self.level)>=14:
                    AS+=1
        if str(self.char_class)== str(classes[8]):
            if int(self.level)>=10:
                AS+=1

        print('\nYou are ' + self.name + ', a level ' + str(self.level) + ' ' + self.char_race + ' ' + self.char_class + '. Your stats are as follows:\n'
              + 'Strength: ' + str(self.strength) + '    modifier  '+str(self.statMod(self.strength))  +'\n'
              'Dexterity: ' + str(self.dexterity) +  '    modifer  '+str(self.statMod(self.dexterity))  +' \n'
              'Intelligence: ' + str(self.intelligence) +  '    modifer  '+str(self.statMod(self.intelligence))  + ' \n'
              'Wisdom: ' + str(self.wisdom) + '    modifer  '+str(self.statMod(self.wisdom))  + ' \n'
              'Charisma: ' + str(self.charisma) +  '    modifer  '+str(self.statMod(self.charisma))  +' \n'
              'Constitution: ' + str(self.constitution) +  '    modifer  '+str(self.statMod(self.constitution))  +' \n\n'
              'Your proficiency Bonus is ' + str(prof) +
              '\nYou have ' + str(AS) + ' ability score improvements to spend\n')
