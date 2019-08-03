# Copyright 2019, Matti Kaupenjohann, All rights reserved.

''' 
This file includes Radius, distance to sun and albedo-value of the Planets of Earth
It checks if the number of values is correctly
Could be extended to other starsystems
 
Sources:
https://astrokramkiste.de/planeten-tabelle
https://de.wikipedia.org/wiki/Albedo
'''
#IMPORT
import warnings

def sun_system(): # Call values for Sun System 
    # Creating an empty planet dictionary 
    PlanetDict = {} 

    # Adding values
    PlanetDict["Planet"] = ["Merkur","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptun"]
    PlanetDict["R"] = [2439500.0,6051500.0,6367500.0,3386000.0,69173000.0,57316000.0,25266000.0,24552500.0] 
    PlanetDict["d"] = [58000000000.0,108000000000.0,150000000000.0,280000000000.0,778000000000.0,1433000000000.0,2872000000000.0,4495000000000.0] 
    PlanetDict["eta"] = [0.119,0.77,0.306,0.25,0.343,0.342,0.3,0.29]  

    len_P = len(PlanetDict["Planet"])
    len_R = len(PlanetDict["R"])
    len_d = len(PlanetDict["d"])
    len_eta = len(PlanetDict["eta"])

    if len_P == len_R &  len_P == len_d & len_P == len_eta:
        pass
    elif len_P != len_R:
        warnings.warn("Length of Radius is not correct")
    elif len_P != len_d:
        warnings.warn("Length of distance is not correct")
    elif len_P != len_eta:
        warnings.warn("Length of eta is not correct")
    else:
        warnings.warn("Strange Behaviour")

    return PlanetDict
