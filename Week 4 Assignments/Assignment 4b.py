# -*- coding: utf-8 -*-
"""
Created on Sun May 30 18:22:38 2021

@author: Uchechukwu
"""
"""
Assignment1
Write a simple statement to implement the usage of each of the 
following dictionary methods
"""
# 1. fromkeys()
position= {'CEO', 'Managing director', 'Operations manager', 'Securty cordinator'}
description= 'Executives'

grouping= dict.fromkeys(position, description)
print(grouping)
print()
#2 get()
login_details= {"mobil_app_pass":" Pweshuche_",
                "gmail_acct_pass":"Pweshius",
                "github_acct_pass":"Pwesh" }
                
print(login_details.get("github_acct_pass"))
print()
#3 items()
login_details= {"mobil_app_pass":" Pweshuche_",
                "gmail_acct_pass":"Pweshius",
                "github_acct_pass":"Pwesh" }
print(login_details.items())

print()
#4 keys()
Qual_details= {"Qualification":"M.Eng",
               "Institution":"Uni of Johannesburg",
               "Year":"2021",
               "Specialization":"AI/Robotics"}
print(Qual_details.keys())

print()
#5 pop()
Qual_details= {"Qualification":"M.Eng",
               "Institution":"Uni of Johannesburg",
               "Year":"2021",
               "Specialization":"AI/Robotics"}
Qual_details.pop("Specialization")
print(Qual_details)

print()
#6 popitem()
login_details= {"mobil_app_pass":" Pweshuche_",
                "gmail_acct_pass":"Pweshius",
                "github_acct_pass":"Pwesh" }
login_details.popitem()
print(login_details)

print()
#7 setdefault()
Qual_details= {"Qualification":"M.Eng",
               "Institution":"Uni of Johannesburg",
               "Year":"2021",
               "Specialization":"AI/Robotics"}
modify= Qual_details.setdefault("Department","Mechanical engineering")
print(modify)
print(Qual_details)

print()
#8 update()
login_details= {"mobil_app_pass":" Pweshuche_",
                "gmail_acct_pass":"Pweshius",
                "github_acct_pass":"Pwesh" }
login_details.update({"laptop_pass":"PreciousUche"})
print(login_details)

print()
#9 values()
Qual_details= {"Qualification":"M.Eng",
               "Institution":"Uni of Johannesburg",
               "Year":"2021",
               "Specialization":"AI/Robotics",
               "Department":"Mechanical engineering"}
print(Qual_details.values())

print()
""" Assignment 2
Write a progam that appends items in apple list  to fruit list using
append method
"""

def enlarge():
     fruit= ['apple']
     apple= ['apple1', 'apple2', 'apple3', 'apple4']
     for app in apple:
        fruit.append(app)
     return(fruit)

print(enlarge())