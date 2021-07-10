#!/usr/bin/env python3

# simple script to chek work my Parking_place app or not)))

import parking

# simply variables for check 
parkin = parking.Parking_place()
unparking_avto = parking.Avto.unparking
unparking_moto = parking.Moto.unparking
unparking_bus = parking.Bus.unparking
one = "moto"
two = "avto"
three = "bus"
choice = None

if __name__ == "__main__": 
    while choice != "1" or "2" or "3":
        parkin.display_parking()
        parkin.park_places()
        print("What vehicle are going in???\n" )
        print("1.Moto\n")
        print ("2.Car\n")
        print ("3.Bus\n")
        print ("4.Unparking Moto\n")
        print ("5. Unparking Avto\n")
        print ("6.Unparkin Bus\n")
        choice = input()
        if choice == "1":
            parkin.park_proces(one)
        elif choice == "2":
                parkin.park_proces(two)
        elif choice == "3":
            parkin.park_proces(three)
        elif choice == "4":
            unparking_moto()
        elif choice == "5":
            unparking_avto()
        elif choice == "6":
            unparking_bus()