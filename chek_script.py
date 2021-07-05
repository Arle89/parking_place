#!/usr/bin/env python3

# simple script to chek work my Parking_place app or not)))

import parking

# simply variables for check 
parkin = parking.Parking_place()
one = "moto"
two = "avto"
three = "bus"
choice = None

if __name__ == "__main__":
    while choice != "1" or "2" or "3":
        parkin.display_parking()
        print("What vehicle are going in???\n" )
        print("1.Moto\n")
        print ("2.Car\n")
        print ("3.Bus\n")
        choice = input()
    if choice == "1":
        parkin.park_proces(one)
    elif choice == "2":
        parkin.park_proces(two)
    elif choice == "3":
        parkin.park_proces(three)