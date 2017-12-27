import secrets
import numpy as np
# Suits follow the Bridge order: Clubs (0), Diamonds (1), Hearts (2), Spades (3).
deck=np.array([['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'],['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'],['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'],['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']])
randomsuit=secrets.choice(range(deck.shape[0]))
suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
randomcard=secrets.choice(range(deck.shape[1]))
yourcard=deck[randomsuit,randomcard]
print('Your card is the ' + yourcard + ' of ' + suit[randomsuit] + '.')


