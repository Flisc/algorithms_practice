import random
""" 
comment Silviu
"""
"""if condition1:          |    for val in sequence:         |      counter = 0
        # code block 1     |        # statement(s)           |      
   elif condition2:        |     else:                       |   while counter < 3:
        # code block 2     |         print("No items left.") |      print('Inside loop')
   else:                   |                                 |          counter = counter + 1
        # code block 3     |                                 |   else:   

"""
def main():
  print("Hello, My Dear Friend! I randomly generated a number between 0 and 100000. Can you find out?\n")

  newNumber = random.randint(0,100000)
  guess = int(input())
  print(guess)

if __name__ == "__main__":
    main()