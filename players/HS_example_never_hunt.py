class Player():
  def __init__(self):
    self.name = "Never Hunt"

  def hunt_choices(self, round_number, current_food, current_reputation, m,
            player_reputations):

    hunt_decisions = ['s' for x in player_reputations]
    return hunt_decisions

  def hunt_outcomes(self, food_earnings):
    pass # do nothing

  def round_end(self, award, m, number_cooperators):
    pass # do nothing
