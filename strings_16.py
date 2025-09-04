name = "anamika"
#string slicing
nameshort= name[0:3] #start from index 0 all the way till 3(exluding 3)
print(nameshort) # Output: ana

#slicing with skip value
nameshort1= name[0:6:2] #start from index 0 all the way till 6(exluding 6)with a skip value of 2
print(nameshort1) 

#strings functions
name= "anamika"
print(len(name)) #tells length of string

print(name.endswith("mika")) #checks if the string ends with mika or not

print(name.startswith("ana")) #checks if the string starts with ana or not

print(name.capitalize()) #capitalizes the first letter of the string

print(name.upper())#converts the string to uppercase

index= name.find("mika") #finds the index of mika in the string
print(index) # Output: 3 

b= "anamika is a good good student"
a=b.replace("good", "bad")
print(a)
