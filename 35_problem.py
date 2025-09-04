#write a program to display details entered by the user that is name , age , gender and height

name=input('enter the name : ')
age= eval(input('enter the age : '))
gender= input('enter the gender :')
height= eval(input('enter the height : '))

''''print('Name:', name)
print('Age:', age)
print('Gender :', gender)
print('Height:', height)

print(type(height))'''

print(f'Name: {name}, Age: {age}, Gender :{gender}, Height : {height}') #f - string formatting
