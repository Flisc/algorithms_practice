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
def numer_digits(number):
     return_arr = []
     while number // 10 > 0:
          return_arr.append(number % 10)
          number = number // 10
     return_arr.append(number)
     return return_arr

def main():
    print("Hello, My Dear Friend! I randomly generated a number between 0 and 100000. Can you find out?\n")

    newNumber = random.randint(0,200)
    newNumberDigits = numer_digits(newNumber)
#     print(newNumber)
#     print(newNumberDigits)
#     return
     
    guess = int(input())
    while guess != newNumber:
        
        if guess < newNumber:          
            print("Your guess is smaller than my number.")
        else:
            print("Your guess is higher than my number.")

        guess_digits = numer_digits(guess)
     #    print(guess_digits)
        for i in range(len(guess_digits) - 1, -1, -1):
             if guess_digits[i] in newNumberDigits:
                  print("The ", guess_digits[i], " is in my number somewhere.")
                  if i < len(newNumberDigits) and guess_digits[i] == newNumberDigits[i]:
                       print("And in the right place.")
                  else:
                       print("But in the wrong place.")
        guess = int(input())
    print("You won! Your guess is equal to my number.")


#   print(guess)

if __name__ == "__main__":
    main()