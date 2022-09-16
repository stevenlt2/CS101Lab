#welcome
print('Welcome to the Flarsheim Guesser!')
print()
print('Please think of a number between and including 1 and 100.')
print()

#variables
remainder_three = 0
remainder_five = 0
remainder_seven = 0

#Remainder for three
remainder_three = int(input('What is the remainder when your number is divided by 3 ?'))
while(remainder_three < 0 or remainder_three >= 3):
    if remainder_three < 0:
        print('The value entered must be 0 or greater')
        
    elif remainder_three >= 3:
        print('The value entered must be less than 3')
        
    remainder_three = int(input('What is the remainder when your number is divided by 3 ?'))

#Remainder for five
remainder_five = int(input('What is the remainder when your number is divided by 5 ?'))
while(remainder_five < 0 or remainder_five >= 5):
    if remainder_five < 0:
        print('The value entered must be 0 or greater')

    elif remainder_five >= 5:
        print('The value entered must be less than 5')

    remainder_five = int(input('What is the remainder when your number is divided by 5 ?'))
    
#remainder for seven
remainder_seven = int(input('What is the remainder when your number is divided by 7 ?'))
while(remainder_seven < 0 or remainder_seven >= 7):
    if remainder_seven < 0:

        print('The value entered must be 0 or greater')
    elif remainder_seven >= 7:
        print('The value entered must be less than 7')

    remainder_seven = int(input('What is the remainder when your number is divided by 7 ?'))

#finding the number
for i in range(1,101):
    if(i%3 == remainder_three and i%5 == remainder_five and i%7 == remainder_seven):
        print('Your number was',i)
        print('How amazing is that?')
        print()


#Do you want to play again loop
game = True
while game:
    answer = input('Do you want to play again? Y to continue, N to quit ==>')
    if answer == "Y" or answer == 'y':
        print('\nPlease think of a number between and including 1 and 100.')
        print()
#remainder for 3
        remainder_three = int(input('What is the remainder when your number is divided by 3 ?'))
        while(remainder_three < 0 or remainder_three >= 3):
            if remainder_three < 0:
                print('The value entered must be 0 or greater')
            elif remainder_three >= 3:
                print('The value entered must be less than 3')
            remainder_three = int(input('What is the remainder when your number is divided by 3 ?'))
#remainder for 5
        remainder_five = int(input('What is the remainder when your number is divided by 5 ?'))
        while(remainder_five < 0 or remainder_five >= 5):
            if remainder_five < 0:
                print('The value entered must be 0 or greater')
            elif remainder_five >= 5:
                print('The value entered must be less than 5')
            remainder_five = int(input('What is the remainder when your number is divided by 5 ?'))
#remainder for 7
        remainder_seven = int(input('What is the remainder when your number is divided by 7 ?'))
        while(remainder_seven < 0 or remainder_seven >= 7):
            if remainder_seven < 0:

                print('The value entered must be 0 or greater')
            elif remainder_seven >= 7:
                print('The value entered must be less than 7')

            remainder_seven = int(input('What is the remainder when your number is divided by 7 ?'))
        
    elif answer == "N" or answer == 'n':
        game = False
        
    
