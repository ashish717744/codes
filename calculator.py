a1 =int(input('enter the first no'))
a2 =int(input('enter the second n0'))
#print('c1={}+c2={}+c3={}+c4={}'.format(sum,diff,mul,div))
print('c1 =add,c2 =diff,c3=mul,c4=div')
b =str(input('enter the operation:c1|c2|c3|c4'))
print(b)
c=b

def add(a1,a2):
    d1 = a1+a2
    
    return d1
def diff(a1,a2):
    d2= a1-a2
   
    return d2
def mul(a1,a2):
    d3= a1*a2
    
    return d3
def div(a1,a2):
    try:
        if a2 ==0:
            return 'cant be zero'
        else:
           d4=  a1//a2
          
           return d4
    except:
         return keyboardinterupt
c1 =add(a1,a2)        
c2=diff(a1,a2)
c3 =mul(a1,a2)
c4=div(a1,a2)


if c == 'c1':
    print(c1)
elif c == 'c2':
    print(c2)
elif c == 'c3':
    print(c3)
elif c in 'c4':
     print(c4)
else:
    print('no option field')
