# Write a Python program to test whether a number is within 100 of 1000 or 2000
n = int(input('enter the no'))
if (n > 100 and n<1000) and n<10000:
    print('the no is in range')
else:
    print('not in range')
