#!/usr/bin/env python3

# simple script to chek work my Parking_place app or not)))

import parking

# simply variables for check 
parkin = parking.Parking_place()
one = parkin.park_proces("moto")
two = parkin.park_proces("avto")
three = parkin.park_proces("bus")
choice = None

if __name__ == "__main__":
    while choice != one or two or three:
        parkin.display_parking()
        print("What vehicle are going in???\n" )
        print("1.Moto\n")
        print ("2.Car\n")
        print ("3.Bus\n")
        choice = input()