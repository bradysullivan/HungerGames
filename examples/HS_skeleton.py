# You may, but are NOT required to, use object-oriented programming (OOP) in your solution.
# If you choose to use OOP, the methods described below should be class instance methods.

# You may put any variables that you wish to maintain at the module level:

my_variable = 0 # Example optional module variable

# Other auxiliary functions are allowed, but your script must implement at least the three
# functions below, no matter what approach you choose to use. For the OOP option, don't
# forget to add 'self' as a first argument of every function.

def hunt_choices(round_number, current_food, current_reputation, m,  player_reputations):
    # The main routine that plays each individual round.

    # You must create an array of variables 'hunt_decisions' and assign an 'h' for hunt or
    # an 's' for slack (i.e., not hunt) to each member of the array; the order of the hunt 
    # decisions in hunt_decisions should correspond to the order of opponents' 
    # reputations in player_reputations.

    # Blank variables or errors will be assigned 's'.

    # The variables passed in to hunt_choices for your use are:
    #     round_number: integer, the number round you are in.
    #     current_food: integer, the amount of food you have.
    #     current_reputation: float (python's representation of real numbers), your current reputation.
    #     m: integer, the threshold cooperation value for this round.
    #     player_reputations: list of floats, the reputations of all the remaining players in the game.
    #                         The ordinal positions of players in this list will be randomized each round.

    # You may use the global syntax to assign values to any global variables you define, as in:

    global my_variable # Example of making optional my_variable global
    my_variable += 1 # Example of incrementing optional global variable my_variable by 1

    return hunt_decisions;

def hunt_outcomes(food_earnings):
    # hunt_outcomes is called after all hunts for the round are complete.

    # Add any code you wish to modify your variables based on the outcome of the last round.

    # The variable passed in to hunt_outcomes for your use is:
    #     food_earnings: list of integers, the amount of food earned from the last hunt.
    #                    The entries can be negative as it is possible to lose food from a hunt.
    #                    The amount of food you have for the next hunt will be current_food
    #                    + sum of all entries of food_earnings.
    #                    The list will be in the same order as the decisions you made in that round.

    pass 
    # pass is a python placeholder for if you want to define a function that doesn't have
    # any other code. You should replace pass with your own code if you want to use this
    # function, otherwise leave it to prevent errors caused by an empty function.

def round_end(award, m, number_cooperators):
    # round_end is called after all hunts for the round are complete.

    # award - the total amount of food you received due to cooperation in the round.
    # Can be zero if the threshold m was not reached.

    # Add any code you wish to modify your variables based on the cooperation that occurred in
    # the last round.

    # The variables passed in to round_end for your use are:
    #     award: integer, total food bonus (can be zero) you received due to players cooperating
    #            during the last round. The amount of food you have for the next round will be
    #            current_food (including food_earnings from hunt_outcomes this round) + award.
    #     number_cooperators: integer, how many players chose to cooperate over the last round.

    pass
