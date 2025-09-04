'''write a program to find out whether a student has passed or failed 
if it requires a total of 40 % and 33% in each subject to pass'''

marks1= float(input("Enter marks of first subject: "))
marks2= float(input("Enter marks of second subject: "))
marks3= float(input("Enter marks of third subject: "))

if(marks1<33 or marks2<33 or marks3<33):
    print("You have failed in one or more subjects, better luck next time")
elif((marks1+marks2+marks3)/3 < 40):
    print("You have failed, your overall percentage is less than 40%")
else :
    print("Congratulations! You have passed the exam")      