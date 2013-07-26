import os
import sys

import random

class GameEngine():
  def __init__(self, players):
    self.num_players = len(players)
    self.max_food = (self.num_players - 1) * 300
    self.players = []
    for p in players:
      self.players.append(Player(p, self.max_food))
    self.living = self.players
    self.dead = []
    self.round = 0
    self.award = 0
    self.m = 0
    self.cooperators = 0
    self.matrix = []
    self.total_hunts = 0

    self.number_of_rounds = 900


  def start(self):
    while not self.check_for_game_end():
      self.play_round()
      self.round += 1

  def play_round(self):
    self.prep_round()
    self.execute_hunts()
    self.calculate_outcomes()
    self.reward_tribe()
    self.check_for_starve()
    #self.status()

  def prep_round(self):
    self.matrix = [[0 for x in xrange(len(self.living))] for x in xrange(len(self.living))]
    self.m = random.randint(0, (len(self.living)*(len(self.living) - 1)))
    random.shuffle(self.living)

  def execute_hunts(self):
    i = 0
    for player in self.living:    # For each player alive we get their "hunt choices"
      reputations = []
      for partner in self.living: # Get all living players' reputation...
        if partner != player:     # Making sure to skip themself.
          reputations.append(partner.reputation())  # To be passed to the player.
      choices = player.module.hunt_choices(self.round, player.food, player.reputation(),
                                           self.m, reputations)
      j = 0
      for choice in choices:
        if j == i:
          j += 1 # Skip self.
        self.matrix[i][j] = choice
        j += 1
    i += 1

  def calculate_outcomes(self):
    outcomes = []
    for player in list(enumerate(self.living)):
      for choice in list(enumerate(self.matrix[player[0]])):  # player[0] returns the number of the player to then lookup in the matrix.
        if choice[0] != player[0]:  # Skip choice where player hunts with self.
          you = choice[1]
          them = self.matrix[choice[0]][player[0]]
          if you == "h" and them == "h":
            outcomes.append(0)
            self.total_hunts += 2
          elif you == "h" and them == "s":
            outcomes.append(-3)
            self.total_hunts += 1
          elif you == "s" and them == "h":
            outcomes.append(1)
            self.total_hunts += 1
          else:  # both == "s"
            outcomes.append(-2)
      player[1].module.hunt_outcomes(outcomes)
      for i in outcomes:
        player[1].food += i

  def reward_tribe(self):
    if self.total_hunts >= self.m:
      reward = 2 * (len(self.living) - 1)
      for p in self.living:
        p.food += reward
        p.module.round_end(reward, self.m, self.total_hunts)

  def check_for_starve(self):
    for p in self.living:
      if p.food <= 0:
        self.dead.append(p)
        self.living.remove(p)

  def status(self):
    print "Current round: " + str(self.round)
    print "Players alive:"
    for p in self.living:
      print "\t" + p.module.name + ": Food("+ str(p.food) +"), Reputation("+ str(p.reputation()) +")"
    print "Players dead:"
    for p in self.dead:
      print "\t" + p.module.name
    print "Award won this round: " + str(self.award)
    print "\n"

  def check_for_game_end(self):
    if len(self.living) <= 1:
      return True
    elif self.round == self.number_of_rounds:
      return True
    else:
      return False



# Class to hold player information and calculate simple stats.
# Also holds the module for calling the AI code behind each.
class Player():
  def __init__(self, module, food):
    self.module = module
    self.food = food
    self.hunts = 0
    self.slacks = 0

  def reputation(self):
    if self.hunts == 0 and self.slacks == 0:
      return 0
    else:
      return self.hunts / (self.hunts + self.slacks)












