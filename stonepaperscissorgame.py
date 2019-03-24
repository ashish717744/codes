import random
print('welcome to rock paper scissor game')
print('1={0} 2={1} 3={2}'.format('scissor','rock','paper'))
yourchoice =int(input("enter the option you want to choose:1|2|3"))


#do not use string for looping using random choice
#alawys use numerical value if taking input from users
list=['scissor','rock','paper']
otherplayerchoice=random.choice(list)
def game(otherplayerchoice,yourchoice):
    if  otherplayerchoice=='rock' and yourchoice ==1:
              return ('you have lost the game')
    elif otherplayerchoice=='scissor' and yourchoice ==1:
              return('no result')
    elif  otherplayerchoice=='paper' and yourchoice ==1:
              return('you have won the game')
    elif otherplayerchoice=='scissor' and yourchoice ==2:
             return('you have won the game')
    elif  otherplayerchoice=='rock' and yourchoice ==2:
              return('no result')
    elif  otherplayerchoice=='paper' and yourchoice ==2:
             return('you have won the game')
    elif  otherplayerchoice=='rock' and yourchoice ==3:
             return('you have won the game')
      
    elif  otherplayerchoice=='scissor' and yourchoice ==3:
              return('you have lost the game')
    elif  otherplayerchoice=='paper' and yourchoice ==3:
             return('no result')
    else:
        return False

print('yourchoice','=',yourchoice)
print('otherplayerchoice','=',otherplayerchoice)
print(game(otherplayerchoice,yourchoice))
