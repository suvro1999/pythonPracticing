#Let's today start with if else


a = 10;
b = 21;
if a > b:
    print ("a is gatter than b");

if a < b:
    print ("a is smaller than b");
#There are output will be "a is smaller than b".

#yes you can't see any output here because there a is less than b so output not showing
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#While loop 
i = 1
while i < 6:
  print(i)
  i += 1
#the output will be 1 to 6 

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# another while loop example/

#for loop iteration

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Another loop iteration example

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": #you can play with conditional statements here...
    continue
  print(x)
