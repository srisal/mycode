#!/usr/bin/env python3 

message = 'Your connection speed is '

speed = float(input("What is your connection speed in Mbps?")) #to accept decimal datatype used is float

#grade the connection speed
if speed >= 200:
    message = message + 'excellent.'
elif speed >= 100:
    message = message + 'very good'
elif speed >= 50:
    message = message + 'good'
elif speed >= 10:
    message = message + 'fair'
else:
    message = message + 'poor'
print(message)
