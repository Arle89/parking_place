# make parking on pure python3 by classes


class Parking_place():
        small = ['empty','empty','empty','empty','empty']  # simple matrix to avoid Numpy
        medium = ['empty','empty','empty','empty','empty'] 
        big = ['empty','empty','empty','empty','empty']
        matrixx = [small,
                medium,
                big]

        def display_parking(self):  # looping this function makes always visble parking_place
            for i in self.matrixx:
                print(i)
        
        def park_proces(self, vtype):  # make 1 function to interact with all types of vehicle/ need to make it smaler
            if vtype == "moto":
                vehicle = Moto()
                vehicle.park_proces()
            elif vtype == "avto":
                vehicle = Avto()
                vehicle.park_proces()
            elif vtype == "bus":
                vehicle = Bus()
                vehicle.park_proces()
            else:
                print("Sorry, T800 what are you doing here???")




class Moto(Parking_place):
    park_place = Parking_place.matrixx # atribute to interact with matrix and not copy it

    def park_proces(self):
        for i in range(0,3):
            for j in range(0,5):
                if self.park_place[i][j] == "empty":
                    print("Here is place for moto, line:{0}, place:{1}".format([i+1],[j+1])) #add "+1"" to wright numbers of line and place
                    self.park_place [i][j] = "moto"
                    #self.park_place[j].insert(self.park_place[i,j].index("empty"), "moto") / first example which was to hard and long
                    break
                elif self.park_place[i][j] != "empty":
                    continue
            break


class Avto(Parking_place):
    park_place = Parking_place.matrixx

    def park_proces(self):
        for i in range(1,3):
            for j in range(0,5):
                if self.park_place[i][j] == "empty":
                    print("Here is place for car, line:{0}, place:{1}".format([i], [j]))
                    self.park_place[i][j] = "avto"
                    break
                elif self.park_place[i][j] != "empty":
                    continue
            break


class Bus(Parking_place):
    park_place = Parking_place.matrixx

    def park_proces(self):
        for i in self.park_place[2]:
            if i == "empty":
                print("Here we go, Big one")
                self.park_place[2] = "\t\t [bus]"
                break
            else:
                print("There is no place for a Bus")
                break
            break