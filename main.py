#Importing "random" module so that random function can be used.
import random

#Declaraton of Day Trip lists to be randomly selected from
destinations = ['Park', 'Beach', 'Mall', 'Bar']
restaurants = ['Italian', 'Mexican', 'Indian', 'Chinese']
transportation = ['Carpool', 'Taxi', 'Uber']
entertainment = ['Movies', 'Escape Room', 'Museum', 'Axe Throwing']
#Boolean condition for the program to end once User is satisfied with Day Trip itinerary.
satisfied = False

#Function that generates random number for index of each list, allowing for a random item from each list to be selected as called.
def randomizer(list):
    index = random.randint(0, len(list) - 1)
    return list[index]

#Function that prints final, user approved trip details.
def finalTrip(finalDest, finalRest, finalTrans, finalEnt):
    print('\nHere are the final trip details. Have fun!\n')
    print(f'Destination - {finalDest}\n')
    print(f'Restaurant - {finalRest} Food\n')
    print(f'Transportation - {finalTrans}\n')
    print(f'Entertainment - {finalEnt}\n')

#What user will see when first running the program. These are the initial random selections.
print('\nPotential Day Trip Idea:\n')

destChoice = randomizer(destinations)
print(f'Destination - {destChoice}\n')
#After a list has ran through the randomizer, the list will remove the item that was selected so long as the list is not empty. This is to prevent duplicate random selections
#when the user has requested a reroll, while simultaneously preventing the user from crashing the program by rerolling too much.
if len(destinations) > 1:
    destinations.remove(destChoice)

restChoice = randomizer(restaurants)
print(f'Restaurant - {restChoice} Food\n')
if len(restaurants) > 1:
    restaurants.remove(restChoice)

transChoice = randomizer(transportation)
print(f'Transportation - {transChoice}\n')
if len(transportation) > 1:
    transportation.remove(transChoice)

entChoice = randomizer(entertainment)
print(f'Entertainment - {entChoice}\n')
if len(entertainment) > 1:
    entertainment.remove(entChoice)

#Request response from User on if the initial trip itinerary is satisfactory
answer = input("\n Are you satisfied with this trip? Yes or No?\n")

if answer == 'Yes' or answer == 'yes':
    finalTrip(destChoice, restChoice, transChoice, entChoice)

#If user is not satisfied (does not input yes), then program will loop reroll requests on specific aspects of the trip until user is satisfied.
else:
    while satisfied == False:
        reroll = int(input('Input the number corresponding to the aspect of the trip you wish to reroll:\n1 for Destination\n2 for Restaurant\n3 for Transportation\n4 for Entertainment\n5 for All\n6 for Finished\n'))
        if reroll == 1:
            destChoice = randomizer(destinations)
            print(f'\nNew Destination - {destChoice}\n')
            if len(destinations) > 1:
                destinations.remove(destChoice)
        elif reroll == 2:
            restChoice = randomizer(restaurants)
            print(f'\nNew Restaurant - {restChoice}\n')
            if len(restaurants) > 1:
                restaurants.remove(restChoice)
        elif reroll == 3:
            transChoice = randomizer(transportation)
            print(f'\nNew Transportation - {transChoice}\n')
            if len(transportation) > 1:
                transportation.remove(transChoice)
        elif reroll == 4:
            entChoice = randomizer(entertainment)
            print(f'\nNew Entertainment - {entChoice}\n')
            if len(entertainment) > 1:
                entertainment.remove(entChoice)
        elif reroll == 5:
            destChoice = randomizer(destinations)
            print(f'\nNew Destination - {destChoice}\n')
            if len(destinations) > 1:
                destinations.remove(destChoice)
            restChoice = randomizer(restaurants)
            print(f'\nNew Restaurant - {restChoice}\n')
            if len(restaurants) > 1:
                restaurants.remove(restChoice)
            transChoice = randomizer(transportation)
            print(f'\nNew Transportation - {transChoice}\n')
            if len(transportation) > 1:
                transportation.remove(transChoice)
            entChoice = randomizer(entertainment)
            print(f'\nNew Entertainment - {entChoice}\n')
            if len(entertainment) > 1:
                entertainment.remove(entChoice)
        elif reroll == 6:
            satisfied = True
            finalTrip(destChoice, restChoice, transChoice, entChoice)