#Write a Python program to count the number 4 in a given list.
#always give input to the lisst 6 7 8 9 9
#if they say give the input in commaseprated then use .split(',')
user =str(input('enter the list'))
user =user.split()
c=0
for i in range(len(user)):   
    if user[i]=='4':
        c=c+1
print(c)    
    
