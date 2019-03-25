print('welcome to the ludo','let start the fucking game',end =' ')
print('1 =blue 2 =green 3=red 4 =yellow')
import random
color =str(input('enter the colour:1|2|3|4'))
color =['1','2','3','4']
player=['1','2','3','4']
dict ={}
for i in random(1,len(color)):
    for j in random(1,len(player)):
        player['j']=color[i]
print('playerno and its color choice')
print(dict)

dice1 =['1','2','3','4','5','6']

def startingturn(dice1):
    add = random.choice(dice1)
    return 0
player1 =startingturn(dice1)
print('player1 result',player1)
player12=startingturn(dice1)
print('player2 result',player2)
player3 =startingturn(dice1)
print('player3 result',player3)

player4 =startingturn(dice1)
print('player4 result',player4)
if player1 == '6':
    print('player1 won and player1 will start the game')
    print('
    player1 =random.choice(dice1)
    if player1 !='6':
        print('take',player1,'step')
     print('   
    
elif player2 =='6':
    print('player2 won and player1 will start the game')
    
elif player3=='6':
    print('player3 won and player1 will start the game')
    
elif player4=='6':
    print('player4 won and player1 will start the game')
    
elif player1=='6' and player2=='6':
    print('player1 and player2 will start the game')
    
elif player1=='6' and player3=='6':
    print('player1 and player3 will start the game')
    
elif player1=='6' and player2=='6':
    print('player1 and player2 will start the game')
    
elif player1=='6' and player2=='6':
    print('player1 and player2 will start the game')

elif player2=='6' and player3=='6':
    print('player2 and player3 will start the game')

elif player2=='6' and player3=='6':
    print('player2 and player3 will start the game')

elif player2=='6' and player4=='6':
    print('player2 and player4 will start the game')

elif player2=='6' and player4=='6':
    print('player2 and player4 will start the game')

elif player3=='6' and player4=='6':
    print('player3 and player4 will start the game')

elif player2=='6' and player4=='6' and player1 =='6':
    print('player2 and player4 and player1 will start the game')



elif player2=='6' and player4=='6' and player3=='6':
    print('player2 and player4 and player3 will start the game')


elif player2=='6' and player1=='6' and player3=='6':
    print('player2 and player1 and player3 will start the game')


elif player3=='6' and player4=='6' and player1=='6':
    print('player1 and player4  and player3 will start the game')

elif player3=='6' and player4=='6' and player1=='6' and player2=='6':
    print('player1 and player4  and player3 and player2 will start the game')

else:
    print('keyboard interupt')
          

try:
    






    
