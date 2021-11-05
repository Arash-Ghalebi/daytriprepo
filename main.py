import random

destinations = ['Park', 'Beach', 'Mall', 'Bar']
restaurants = ['Italian', 'Mexican', 'Indian', 'Chinese']
transportation = ['Carpool', 'Taxi', 'Uber']
entertainment = ['Movies', 'Escape Room', 'Museum', 'Axe Throwing']
satisfied = False

def randomizer(list):
    index = random.randint(0, len(list) - 1)
    return list[index]

def finalTrip(finalDest, finalRest, finalTrans, finalEnt):
    print('\nHere are the final trip details. Have fun!\n')
    print(f'Destination - {finalDest}\n')
    print(f'Restaurant - {finalRest} Food\n')
    print(f'Transportation - {finalTrans}\n')
    print(f'Entertainment - {finalEnt}\n')

print('\nPotential Day Trip Idea:\n')

destChoice = randomizer(destinations)
print(f'Destination - {destChoice}\n')

restChoice = randomizer(restaurants)
print(f'Restaurant - {restChoice} Food\n')

transChoice = randomizer(transportation)
print(f'Transportation - {transChoice}\n')

entChoice = randomizer(entertainment)
print(f'Entertainment - {entChoice}\n')

answer = input("\n Are you satisfied with this trip? Yes or No?\n")

if answer == 'Yes' or answer == 'yes':
    finalTrip(destChoice, restChoice, transChoice, entChoice)

else:
    while satisfied == False:
        reroll = int(input('Input the number corresponding to the aspect of the trip you wish to reroll:\n1 for Destination\n2 for Restaurant\n3 for Transportation\n4 for Entertainment\n5 for All\n6 for Finished\n'))
        if reroll == 1:
            destChoice = randomizer(destinations)
            print(f'\nNew Destination - {destChoice}\n')
        elif reroll == 2:
            restChoice = randomizer(restaurants)
            print(f'\nNew Restaurant - {restChoice}\n')
        elif reroll == 3:
            transChoice = randomizer(transportation)
            print(f'\nNew Transportation - {transChoice}\n')
        elif reroll == 4:
            entChoice = randomizer(entertainment)
            print(f'\nNew Entertainment - {entChoice}\n')
        elif reroll == 5:
            destChoice = randomizer(destinations)
            print(f'\nNew Destination - {destChoice}\n')
            restChoice = randomizer(restaurants)
            print(f'\nNew Restaurant - {restChoice}\n')
            transChoice = randomizer(transportation)
            print(f'\nNew Transportation - {transChoice}\n')
            entChoice = randomizer(entertainment)
            print(f'\nNew Entertainment - {entChoice}\n')
        elif reroll == 6:
            satisfied = True
            finalTrip(destChoice, restChoice, transChoice, entChoice)