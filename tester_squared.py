# This test program should identify the common mistakes
# that you can make, and suggest how you can fix them.
# There are many other things that can be checked, and
# we advise you to add the test cases yourself.

# HOW TO EXECUTE:

# If you are using python shell:
#   import tester
#   tester.run_tests('filename_of_your_script.py')
# If you are using the command line:
#   python tester.py filename_of_your_script.py


import sys
import importlib

import tester

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print ("\nYou must include the filename that contains your players "
               "as the only argument to this script.\n\n"
               "Example: python tester.py players.txt\n")
        raise
    else:
        run_tests(filename)

def compareAIs():
  print("Comparing AIs")



