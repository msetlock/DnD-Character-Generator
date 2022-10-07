from player import player
import random
import tkinter

statVals = [15, 14, 13, 12, 10, 8]
random.shuffle(statVals)


all_races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf',
                 'halfling', 'Half-Orc', 'Human', 'Tiefling', 'Leonin', 'Satyr', 
                 'Owlin', 'Aarakocra', ' Aasimar', 'Air Genasi', 'Bugbear', 'Centaur', 'Changeling',
                 'Deep Gnome', 'Duergar', 'Earth Genasi', 'Eladrin', 'Fairy','Firbolg', 'Fire Genasi', 'Githyanki'
                 ,'Githzerai', 'Goblin', 'Goliath', 'Harengon','Hobgoblin', 'Kenku', 'Kobold', 'Lizardfolk', 
                 'Minotaur','Orc','Sea Elf', 'Shadar-kai','Shifter', 'Tabaxi', 'Tortle','Triton', 'Water Genasi',
                 'Yuan-Ti', 'Feral Tiefling'  ]

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
           'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'Artificer']


playerChar = player(random.choice(all_races), 'Bard', 0,
                       statVals.pop(), statVals.pop(), statVals.pop(), statVals.pop(), statVals.pop(),statVals.pop())


#top = tkinter.Tk()
# Code to add widgets will go here...
playerChar.setName()
playerChar.setLevel()
playerChar.rundown()

""" generate = tkinter.Button(top, text='Generate new Hero', command=newChar(playerChar))
generate.pack()
top.mainloop() 
 """