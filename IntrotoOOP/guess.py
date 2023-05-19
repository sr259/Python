print("Think of a number from 1 to 100 but don't tell me!")
print("I'm going to guess it, but I need you to respond.")
print("to each question with character 'C', 'L', or 'H'.")
print( )

lowestPossible = 1
highestPossible = 100
found = False
guessCount = 0
while not found:
    guess = (lowestPossible + highestPossible) // 2
    prompt = 'Is ' + str(guess) + ' (C)orrect, too (L)ow, or too (H)igh? '
    feedback = input(prompt).strip()
    if feedback in ('C','L','H'):
        guessCount += 1
        if feedback == 'C':
            found = True
        elif feedback == 'H':
            highestPossible = guess - 1
        else:
            lowestPossible = guess + 1
    else:
        print('Invalid response')
print('I found it in', guessCount, 'guesses!' if guessCount > 1 else 'guess!')
