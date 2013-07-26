from game import GameEngine
import sys
import os
import importlib


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print ("\nYou must include the filename that contains your players "
               "as the only argument to this script.\n\n"
               "Example: python tester.py players.txt\n")
        raise

    players = []
    f = open(filename,'r')
    for script_name in f:
        try:
            user_module = importlib.import_module(script_name[:-4])
            if hasattr(user_module, 'Player'):
                try:
                    user_module = user_module.Player()
                except:
                    print("\nPlayer did not instantiate, make sure it is a class. "
                          "Proceeding assuming non OO code.\n")
        except:
            print ("\nCould not import %s\n" % script_name)
            raise
        players.append(user_module)

    winners = []

    for i in range(0, 10000):
      game = GameEngine(players)
      game.start()
      winners.append(game.living)

    asdf = {}

    for i in winners:
      x = i[0]
      if x.module.name in asdf.keys():
        asdf[x.module.name] += 1
      else:
        asdf[x.module.name] = 1

    for i in asdf.keys():
      print i + ": " + str(asdf[i])
