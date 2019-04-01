#Write a Python program to check whether a file exists.

#Sample Solution:-

#Python Code:

import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))
