# Copyright 2019, Matti Kaupenjohann, All rights reserved.

'''
Script for calculating Temperature of Earth 
(For Flatearther and other idiotic guys) 
The user can choose any Planet that is loaded
with the planetfile to calculate the
Equilibrium temperature 
 
Sources:
https://de.wikipedia.org/wiki/Gleichgewichtstemperatur
'''
#IMPORT
from sympy.solvers import solve
from sympy import Symbol
from colorama import init 
from termcolor import colored
import math
import importlib
import planets
import constants

#Colors for CMD
init()

PlanetDict = planets.sun_system()
print(colored("Do you want to see available Planets? [Y/N] ",'blue'))
choice = input("Your Awnser: ").lower()



# input returns the empty string for "enter"
yes = {"yes","ye","y","ja","j"}
no = {"no","n","nein"}

if choice in yes:
    print(colored(PlanetDict["Planet"],'green'))
elif choice in no:
    print(colored("Truly wonderful, the mind of a child is.",'yellow'))
else:
    print(colored("Please respond with 'yes' or 'no'",'magenta'))

print(colored("Choose Your Planet ",'blue'))
planet_choice = input("Your Awnser: ")

try:
    planet_idx = PlanetDict['Planet'].index(planet_choice)
except:
    print(colored("You need to choose a available Planet",'red'))
else:
    T = Symbol('T')
    R = PlanetDict["R"][planet_idx]
    d = PlanetDict["d"][planet_idx]
    eta = PlanetDict["eta"][planet_idx]

    L_in = (1-eta)*(math.pi*R**2*constants.L_sun)/(4*math.pi*d**2)
    L_out = (4*math.pi*R**2*constants.sig*T**4)

    T_K  = solve(L_in - L_out, T) 
    T_C = T_K[1]-273.15
    print(colored("Equilibrium temperature on "+planet_choice+":",'cyan')) 
    print(colored(str(T_K[1])+" K",'cyan'))
    print(colored(str(T_C)+"° C",'cyan'))

