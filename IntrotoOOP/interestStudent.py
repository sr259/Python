##################################################################
# Student contributions to the interest calculator
#
# You are free to add additional utility functions as you see fit,
# but you must implement each of the following functions while
# adhering to the specifications given in the project description
##################################################################

#---------------------------------------------------------------------------------
def greeting():
    print("""
This interest calculator will ask you to select an interest rate,
followed by a principal value.  It will then calculate and display
the principal, interest rate, and balance after one year.
You will then be invited to execute the process again or terminate.
    """)

#---------------------------------------------------------------------------------

def getRate(choices):
    done  = False
    while done == False:
            letter = ['A', 'B', 'C', 'D', 'E', 'F']
            for i in range(len(choices)):
                print(letter[i] +') ', str(choices[i]) + '%')
            choice = input('Enter' + ' ' + letter[0] + '-' + letter[len(choices) - 1] + ':')
            if choice in letter:
                location = letter.index(choice)
                done = True
                return choices[location] / 100
            else:
                print()
                print('This is not a valid selection')
                print()

#---------------------------------------------------------------------------------

def getPrincipal(limit):

    while True:
        value = input('Enter the principal (limit ' + str(limit) +'): ')
        if value[0] == '$':
            value = value[1:]
        try:
           float(value)
        except:
            print("Value not properly entered in dollars and cents")
            continue
        if value == '69':
            print()
            print('Nice.')
            return value

        if value != "{:.2f}".format(float(value)):
            if value != "{:.1f}".format(float(value)):
                if not float(value).is_integer():
                    print('There needs to be at most two digits after the decimal')
                    continue
        if float(value) < 0 and float(value) > limit:
            print('Please enter a number between 0 and {limit}')
            continue
        return float(value)



#---------------------------------------------------------------------------------

def computeBalance(principal, rate):
    balance = principal + (principal * rate)
    return balance

#---------------------------------------------------------------------------------

def displayTable(principal, rate, balance):
    line1 = 'Initial Principal   Interest Rate   End of Year Balance'
    line2 = '======================================================='
    line3 = f'{principal:17}   {rate:13}   {balance:18}'
    print(line1)
    print(line2)
    print(line3)

#---------------------------------------------------------------------------------

def askYesNo(prompt):
    done = False
    while done == False:
        answer = input(prompt)
        if answer[0].lower() == 'y':
            done = True
            return True
        if answer[0].lower() == 'n':
            done = True
            return False
        if answer[0].lower() != 'y' and answer[0].lower() != 'n':
            print('Please answer "Y" or "N"')
            done =False

#---------------------------------------------------------------------------------
