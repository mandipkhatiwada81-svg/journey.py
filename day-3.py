# STRINGS

name1 = "Max"
name2 = 'Max'
name3 = '''Max'''
print(name1,name2,name3)


name = "Mandip"
namelen = name[0:5] # start from index 0 all the way till 5 (Excluding 5)
print(namelen)
print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:6])
print(name[1:6])

#positive number (0,1,2,3,4,5,6...)
#negetive number(mandip(-6,-5,-4,-3,-2,-1))


#skip value 
word = "techniques"
print(word[1:8:2]) #ehiu


#Len () function
word1 = "techniques"
print(len(word1))


#escape seq
a = "I am a student of nepal\nlearning python for the future"
b = "I am a student of nepal\nlearning python for the \"future\""
c = "I am a student of nepal\t learning python for the \"future\""
d = 'I am a student of nepal\nlearning python for the \'future\''
e = "I am a student of nepal\nlearning python for the 'future'"
print(a)
print(b)
print(c)
print(d)
print(e)




# practice set


# Write a python program to display a user entered name followed by Good Afternoon using input() function
f = input("Enter your name: ")
print(f"Good Afternoon {f}")
print("Good Afternoon",f)


# Program that is quit hard...

letter = '''Dear <|Name|>,
You are selected!
<|Date|>''' 

print(letter.replace("<|Name|>","Mandip").replace("<|Date|>","23 magh 2085"))


# Write a program to derect double space in a string

abc = ("I am learning  python")
print(abc.find("  ")) # Output is 13 because here is double space. 
print(abc) # Strings are immutable which means that you cannot change then by running functions on then.

abcd = ("I am learning python")
print(abcd.find("  ")) # if the is -1 them there is no duble space


#Replacing the double space into single space

abc = ("I am learning  python")
print(abc.replace("  ", " "))




# this proble is given by chatgpt

#letter_1 = "Dear Max, this python course is nice. Thanks"
letter_1 = "Dear Max,\nthis python course is nice.\nThanks"
print(letter_1)

