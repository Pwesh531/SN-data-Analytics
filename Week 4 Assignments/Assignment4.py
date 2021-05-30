# -*- coding: utf-8 -*-
"""
Created on Sun May 30 17:43:09 2021

@author: Uchechukwu
"""

""" Question 1
Write a loop statement that prints out numbers between 1 & 20 
                        
"""
for number in range(1,21):
    print(number)
    
print()
"""Question 2
Write a simple loop that prints out even numbers between 30 and 70
"""
for number in range(30, 71):
    if number % 2 == 0:
        print(number)

print()
""" Question 3
Write a loop that prints multiplication table 5
"""
count=1
for number in range(1, 13):
    result= 5 * count
    count += 1
    print(result)
    
print()
"""Question 4
Write a program that accepts number input from a user and return the 
factorial of that number
"""
def fac():
    number= int(input('Please enter a number '))
    for reduction in range(1, number):
        number = number * reduction
    return number
print(fac())



