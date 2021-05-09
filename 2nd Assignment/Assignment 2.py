# -*- coding: utf-8 -*-
"""
Created on Wed May  5 23:29:51 2021

@author: Uchechukwu
"""

# Question 1- How do I convert the string "1000" to an integer
#Answer - Use the int() function as illustrated below
print(int("1000"))

# Question 2- How do I convert the floating point number 3.764 to and integer
#Answer- Use the int() function as illustrated below
print(int(3.764))

#Question 3
expenses= str(99.45)
print("$" + expenses + " " + "dollars" )

#Question 4
"""Answer-  The type function returns the class of whatever object passed into it.
for example... 
print(type(expenses)) returns <class 'str'>"""

#Question 5
""" Answer- A Boolean is a datatype that can either be True or False.
The two possible values are True or False """

#Question 6
"""Answer-  The technical name for the % opeator is Modulo. It returns the the 
remainder obtained from dividing the left hand operand by the right hand operand
"""

#Question 7
fancy_name= str("Ukaegbu Uchechi")
print(fancy_name)

#Question 8
Time_hour= int(input("Please enter the time in hours "))
Conversion_seconds= Time_hour * 3600
print("Your time in seconds is", Conversion_seconds)

#Question 9
def easy_money():
    print(int(100))
easy_money()


def best_food_ever():
    print("Sushi")
best_food_ever()

def convert_to_currency(a:int):
    amount = str(a)
    return "$" + amount
    
print(convert_to_currency(10))

#Question 10
def string_adder(a=" ", b= " "):
    return print(a + " " + b)
string_adder("Pwesh", "Uche")
string_adder()

#Question 11
def long_word(s=" "):
    print(len(s)>7)
long_word("Uchechukwu")
long_word("Uche")

#Question 12
def same_and_first_last_letter(f:str):
    print(f[0] == f[-1])
same_and_first_last_letter("uchechukwu")
same_and_first_last_letter("Uche")  

#Question 13
def first_three_characters(t:str):
    print(t[0] + t[1] + t[2])
first_three_characters("Uchechi")
    
  

