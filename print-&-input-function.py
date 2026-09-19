# 19/09/2026

print("GAYATRI BARLE")
print(8+5)
# print(hello)  in that case we get "name_error" so if we 
# want to print any santences then we have to use double qoutes - "".

print(8)     # this code is run because its number. 

# we can performe mathematic task through print function, 
# but we can't access task's value again because its temporary, 
# print function is just print the values on terminal not store it.

print(8+6-4*2+5*0)
print((8*2)+ 6 / 2 + 10 -9)

#print function with input function.

print(input("enter 1st number= " +  "enter 2nd number= " )) 
#this code run but not perform the task, so we need two input.
print(input("enter 1st number= ") + input("enter 2nd number= "))
# this code is run but, as we know that input is a string type 
# it cant add any number its concnate it to each other 

# so we need to change the type of input, 
# we use type convertion method for adding any number if its integer.

int(input("enter your number= "))  # this is the method of type converton.

print(int(input("enter 1st num = ")) + int(input("enter 2nd num = ")))

#we can also write  like this 
print(int(input("enter 1st num = ") + input("enter 2nd num = ")))
# but again its not work its concnate the numbers to each other.


# so that why we need variables thats store and accessable.