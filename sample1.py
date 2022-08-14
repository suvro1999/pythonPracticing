print ("Hello world!")
a = 20
print (a)
b = 19.48
print (b)
#This is the basic of python syntax to print a string,intger, float
#Number type data Like intger float, complex,random number
num1,num2,num3, text1 = 121, 12.232, 3j,"Those are example of "
print (text1, num1,num2,num3)
#Type casting 
a = int(a)
c = int(33.93)
d = float(23)
e = str("hell01")
print (a,b,c,d,e)

#String 
#You can use multiple string in a variable with triple """Coma""" let's try
a = """This is example of 
     Multiple string so we 
     can white multile string in 
     python with help of Triple coma."""
print(a)

#Normal String 
x = "A normal string"
print(x) #Out put will be "A normal string".

#Slicing string
b = "Hello, World!"
print(b[2:5]) #Out put will be "llo" you can control which index will be print
#Index of "Hello, world" |h[0]|e[1]|l[2]|l|o|,| |W|o|r|l|d|![n]| 

#modify String There you can create Uppercase,lowercase,remove,replace etc in a string
a = "Hello, World!"
print(a.lower())
print(a.upper())

#Format string 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#String methon There have many string method to learn you can learn more on
#  https://www.w3schools.com/python/python_strings_methods.asp

#For boolen 
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#operators
# +	        Addition	             x + y	
# -	        Subtraction	             x - y	
# *	        Multiplication	         x * y	
# /	        Division	             x / y	
# %	        Modulus	                 x % y	
# **	    Exponentiation	         x ** y	
# //	    Floor division           x // y

#I think you can play with operators now 


#Sort list is used for store multiple value
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
