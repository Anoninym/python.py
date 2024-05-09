# Prompt the user for a number either on a form input or the terminal.
#  Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
num = float(input('enter any number? '))
if num % 2 == 0:
    print('the number is even')
else:
    print('the number is odd')