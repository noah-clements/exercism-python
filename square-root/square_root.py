# Babylonian? method
def square_root(number):
    guess = number / 2
    while True:
        new_guess = (guess + number / guess) / 2
        if abs(guess - new_guess) < 0.00000001:
            return new_guess
        guess = new_guess

