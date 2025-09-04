#printing absolute value of a number entered by user using function 

def absolute_value(num):
    if num>=0:
        return num
    else: 
        return (-num)

number = eval(input('Enter an number :'))
print('the absolute value of the entered number is :', (absolute_value(number)))
