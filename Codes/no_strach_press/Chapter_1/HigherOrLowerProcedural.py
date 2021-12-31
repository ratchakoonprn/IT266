#  HigherOrLower

import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pops one off the top of the deck and returns it
    return thisCard
    
# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

#  Main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

startingDeckList = []
for suit in SUIT_TUPLE: # สำหรับไพ่แต่ละแบบ โพ, หัวใจ, ข้าวหลามตัด, ดอกจิก รวม 4 ตัว
    for thisValue, rank in enumerate(RANK_TUPLE): # RANK_TUPLE ค่าของไพ่มี 13 ค่า eg. thisValue = 0, rank = 'Ace'
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict) 
        # {'rank':'Ace', 'suit':'Spades', 'value':1} ใบที่ 1
        # ....
        # {'rank':'Ace', 'suit':'Spades', 'value':13} ใบที่ 13
        
score = 50

while True:  # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList) # สับไพ่
    currentCardDict = getCard(gameDeckList) # แสดงไพ่ใบแรก
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']    
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):   # play one game of this many cards
        answer = input('Will the next card be higher or lower than the ' + 
                               currentCardRank + ' of ' + 
                               currentCardSuit + '?  (enter h or l): ')
        answer = answer.casefold()  # force lower case
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15          

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue  # don't need current suit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')


    
    



         

    
