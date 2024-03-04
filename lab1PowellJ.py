ONES_VAL = 1.0
FIVES_VAL = 5.0
TENS_VAL = 10.0
TWENTIES_VAL = 20.0

PENNY_VAL = 0.01
NICKEL_VAL = 0.05
DIME_VAL = 0.10
QUARTER_VAL = 0.25

ones = int(input('Input number of ones: '))
fives = int(input('Input number of fives: '))
tens = int(input('Input number of tens: '))
twenties = int(input('Input number of twenties: '))

pennies = int(input('Input number of pennies: '))
nickels = int(input('Input number of nickels: '))
dimes = int(input('Input number of dimes: '))
quarters = int(input('Input number of quarters: '))

total = ones * ONES_VAL + fives * FIVES_VAL + tens * TENS_VAL + \
    twenties * TWENTIES_VAL + pennies * PENNY_VAL + \
    nickels * NICKEL_VAL + dimes * DIME_VAL + quarters * QUARTER_VAL

print('Your profit is: $%10.2f' % total)
