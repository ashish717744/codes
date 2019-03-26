#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
#Sample value of n is 5 
#Expected Result : 615
n = int(input('enter the input'))
list =[n,n,n,n,n,n]

list[1] =list[[1]+[2]]
print(list[1])
list[3]=list[4]+list[5]+list[3]

list[0] =list[1]+list[0]
list[0] =list[0]+list[3]
print(list)

