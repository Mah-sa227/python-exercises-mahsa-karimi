import random
ran=random.choice(['sang','kaqaz','qeychi'])

while True:

    game=input(' sang  kaqaz  qeychi exit : ').lower()
    x='exit'
    
    if game==x:
        print('bye')
        break
    
    elif ran!=game:
        print('game over try again :')
        continue
    
    else:
        ran==game
        print('you win ... ')
        break
    