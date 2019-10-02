#! /usr/bin/env python

import csv
import random
import re

class AERandomizer:
  def __init__(self):
    self.market = False
    self.nemesis = False
    self.mages = False
    self.expedition = {}
    self.exclusions = {}

  def begin_expedition(self):
    #When starting an expedition, the following happens:
    # Draw 3 Gems, 2 Relic, 4 Spells - Into Barracks
    # Draw 4 mages, add to Barracks
    # Nemesis - Tier 1
    self.expedition['nemesis'] = self.get_nemesis(tier='1')

    self.expedition['mages'] = []
    #Duplicate mage logic
    for _ in range(4):
      selected_mage = self.get_mage()

      #Check for duplicates
      for _mage in self.expedition['mages']:
        while _mage[0] == selected_mage[0]:
          print("Duplicate mage, reselecting {0}".format(_mage[0]))
          selected_mage = self.get_mage()

      self.expedition['mages'].append(selected_mage)
    
    #Cards now

    return self.expedition
  
  def lost_expedition(self, to_draw=False):
    if to_draw == 'mage':
      return
    elif to_draw in ['gem', 'relic', 'spell']:
      return
    else:
      print("Card to draw not defined")
      return

  def win_expedition(self):
    #Draw the following:
    # One Gem, Relic, Spell to Barracks
    # Win Tier 1 - 5 random level 1 treasures
    # Win tier 2 - 3 random level 2 treasures
    # Win tier 3 - 5 random level 3 treasures
    return


  def _load_nemesis(self):
    self.nemesis = { '1': [], '2': [], '3': [], '4': []}
    with open('data/nemesis.csv') as csvfile:
      nemesis_data = csv.reader(csvfile)
      for _nemesis in nemesis_data:
        #Removing anything commented out in the CSV files
        if not re.search(r'^#',_nemesis[0]):
          current_nemesis = [_nemesis[0], _nemesis[2], _nemesis[1]]

          #Any notes we may want displayed
          if len(_nemesis) == 4:
            current_nemesis.append(_nemesis[3])

          self.nemesis[_nemesis[1]].append(current_nemesis)
    return
  
  def _load_mages(self):
    self.mages = []
    with open('data/mages.csv') as csvfile:
      mage_data = csv.reader(csvfile)
      for _mage in mage_data:
        current_mage = [_mage[0],_mage[1]]
        self.mages.append(current_mage)
    return

  def get_mage(self):
    if not self.mages:
      self._load_mages()
    return random.choice(self.mages)

  def get_nemesis(self, tier=False):
    #Check to see if the nemesis list has been loaded
    if not self.nemesis:
      #Otherwise, load it
      self._load_nemesis()
    
    if tier:
      chosen_nemesis = random.choice(self.nemesis[tier])
      return chosen_nemesis
    else:
      chosen_nemesis = random.choice(self.nemesis[str(random.randrange(1,5))])
      return chosen_nemesis

