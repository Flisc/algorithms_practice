import random
""" 
"""
"""if condition1:          |    for val in sequence:         |      counter = 0
        # code block 1     |        # statement(s)           |      
   elif condition2:        |     else:                       |   while counter < 3:
        # code block 2     |         print("No items left.") |      print('Inside loop')
   else:                   |                                 |          counter = counter + 1
        # code block 3     |                                 |   else:   

Hello, My Dear Friend! I randomly generated a number between 0 and 100000. 
Can you find out?

Give me a guess, please!
4 //input

Your guess is smaller than my number.
The 4 is in my number somewhere.
And in the right place.

Give me a guess, please!
6532 //input

Your guess is smaller than my number.
The 3 is in my number somewhere.
And in the right place.
The 2 is in my number somewhere.
But in the wrong place.

"""

def main():
  print("Hello, My Dear Friend! I randomly generated a number between 0 and 100000. Can you find out?\n")

  newNumber = random.randint(0,100000)
#   guess = int(input())
#   print(guess)

if __name__ == "__main__":
    main()