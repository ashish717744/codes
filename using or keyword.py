# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. Go to the editor
n =int(input('enterno'))
n1 =int(input('enter the second no'))
def user(n,n1):
   if n==n1 or n-n1==5 or n1-n==5 or n+n1==5:
      return True
print(user(n,n1))
