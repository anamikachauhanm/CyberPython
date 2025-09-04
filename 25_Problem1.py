#write a python prograam that calculates the time that a car will take to travel a certain distance
x= speed = float(input("enter the speed of the car in km/hr :"))
y = distance = float(input("enter the distance to be travelled in km :"))
time = distance / speed
print("The time taken to travel", distance, "km at a speed of", speed, "km/hr is", time, "hours")