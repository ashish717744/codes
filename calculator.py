from math import log

print('1 =add,2 =diff,3=mul,4=div,5 =log')
#for log str is not working if i m giving c5 then also its not going to if loop. so for this i m using int.

b =int(input('enter the operation:1|2|3|4|5'))

try:
    if b==5:
        b1=int(input('enter the no for log'))
     
        def log1(b1):
            return  log(b1)
        print('log','=',log1(b1))

    

except:
    a1 =int(input('enter the first no'))
    a2 =int(input('enter the second n0'))
#print('c1={}+c2={}+c3={}+c4={}'.format(sum,diff,mul,div))


           
     
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
           


    if b == 1:
        print(c1)     
    elif b == 2:
        print(c2)
    elif b == 3:
        print(c3)
    elif b in 4:
         print(c4)
    else:
        print('no option field')
    
