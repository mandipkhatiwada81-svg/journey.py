# Today I'll learn VARIABLES AND DATATYPE

#VARIABLES
print("What is variables? ")
print("Variables is the name give to memory location in a program.")

a = 20
b = 30
c = "ZEYRO"
print( a + b ,",",a -b)
print(c)
# In this program a,b and c are the variables because they contine values or data.



#DATATYPE
# 1. Integers(int) = 1, 2, 3, 4.........
# 2. Floating point number(float) = 1.1, 23.34, 324.23........
# 3. Strings(str) = "Harry", "Max", "Lisa", "Nepal" etc.
# 4. boolean = True or False
# 5. None = nothing




#OPERATORS IN PYTHON
# 1. Arithmetic operators: +,-,*,/ etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not.


# Arithmetic operators

d = 3
e = 4
f = d+e
print(c)


# Assignment operators
g= 4-2 #assign 4-2 in a
print(a)
h = 6
h += 3 # Increment the value of b by 3 and then assign it to b
#h -= 3 # Decrement the value of b by 3 and then assign it to b
print(h)


# Comparison operators
i = 6 > 5 
print(i)

j = 6 < 5
print(j)

k = 4<4
print(k)

# Logical operators

# Truth table of "AND"
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Truth table of "OR" 
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Truth table of "NOT" 
print(not True)   # False
print(not False)  # True



#TYPE
l = "Max"
t = type(l) #class <str>
print(t)

m = 23
t = type(m) # class <int>
print(t)

n = 1.1111
t = type(n) # class <float>
print(t)

o = "12"
p = int(o) # chaning the type
t = type(p)
print(t)

#r = "yooo"
#u = int(r) # we can not change str to int
#t = type(u)
#print(t)




# INPUT

q = input("Enter your name: ")
r = input("What is your fov game: ")
print(q)
print(r)
s = int(input("Enter the number 1: "))
u = int(input("Enter the number 2: "))
print("The sum of two number is", s + u)





# Day 2 is over now. Let's practice.....

#write the program to add two numbers

v = 1
w = 2
print("The sum of v and w: ",v + w) # that's all



# Write the program to find remainder when a number is divided by z

x = int(input("Enter the number one: "))
y = int(input("Enter the number two: "))
print("The remainder of number is: ", x % y) # to find the remainder we need to use "%"


# Check the type of variable assigned using input () function.

a1 = input("Enter the value of oo: ")
print("The type is", type(a1))




# Use comparison operator to find the a is greater them b 

c1 = int(input("Enter the value of a: "))
d1 = int(input("Enter the value of b: "))
print("a is greater then b", c1 > d1)



# write the program to find an average of the numbers entered by the user. 
e1 = float(input("Enter the value of a: "))
f1 = float(input("Enter the value of b: "))
print("The average of two number is ", (e1 + f1)/2 )




# write the program to calculate the square of a numbers entered by the user. 
g1 = float(input("Enter the first number: "))
print("The square of the number is",g1**2) # we can use g1 * g1 also
#print("The square of the number is",g1^2) # Incrrect for finding square of a number in Python


# now i am done byee bye guys see you soon......


