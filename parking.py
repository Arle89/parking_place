# make parking on pure python3 by classes


class Parking_place():
        small = [ "empty", 'empty','empty','empty','empty']  # simple matrix to avoid Numpy
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

        def park_places(self):
            count_moto = 0
            count_avto = 0
            count_bus = 0
            count_empty = 0
            for i in self.matrixx:
                for j in i:
                    if j == "avto":
                        count_avto += 1
                    elif j == "moto":
                        count_moto += 1
                    elif j == "Bus":
                        count_bus += 1
                    elif j == "empty":
                        count_empty += 1
                    else:
                        print("Parking is full !!")
        
            return print("MOTO vehicle is: ",count_moto, "\n", "AVTO vehicle is: ",count_avto,"\n", "BUS vehicle is: ", count_bus, "\n", "EMPTY is: ",count_empty )




class Moto(Parking_place):
    park_place = Parking_place.matrixx # atribute to interact with matrix and not copy it
    place = []

    def __str__(self):
        return f"moto"

    def __repr__(self):
        return "moto"

    def park_proces(self):
        for i in range(0,3):
            for j in range(0,5):
                if self.park_place[i][j] == "empty":
                    print("Here is place for moto, line:{0}, place:{1}".format([i+1],[j+1])) #add "+1"" to wright numbers of line and place
                    self.park_place [i][j] = "moto"
                    #self.park_place[j].insert(self.park_place[i,j].index("empty"), "moto") / first example which was to hard and long
                    self.place.append(i)
                    self.place.append(j)
                    break
                elif self.park_place[i][j] != "empty":
                    continue
            break
    @staticmethod
    def unparking():
        place = Moto.place
        print ("Place", place[0]+1, place[1]+1, "is empty now")
        Parking_place.matrixx[place[0]][place[1]] = "empty"




class Avto(Parking_place):
    park_place = Parking_place.matrixx
    place = []

    def __str__(self):
        return f"avto"

    def __repr__(self):
        return "avto"


    def park_proces(self):
        for i in range(1,3):
            for j in range(0,5):
                if self.park_place[i][j] == "empty":
                    print("Here is place for car, line:{0}, place:{1}".format([i+1], [j+1]))
                    self.park_place[i][j] = "avto"
                    self.place.append(i)
                    self.place.append(j)
                    break
                elif self.park_place[i][j] != "empty":
                    continue
            break
    @staticmethod
    def unparking():
        place = Avto.place
        print ("Place", place[0]+1, place[1]+1, "is empty now")
        Parking_place.matrixx[place[0]][place[1]] = "empty"




class Bus(Parking_place):
    park_place = Parking_place.matrixx
    place = []

    def __str__(self):
        return f"Bus"

    def __repr__(self):
        return "Bus"


    def park_proces(self):
        empty = []
        for i in range(0,5):
            if self.park_place[2][i] == "empty":
                empty.append(i)
                self.place.append(self.matrixx[2][i])
                if len(empty) == 4:
                    print("Here we go, Big one")
                    self.park_place[2] = "\t\t [bus]"
                    break
                else:
                    continue
            else:
                print("There is no place for a Bus")
                break
            break


    @staticmethod
    def unparking():
        place = Bus.place
        print ("Place", {0}, {1}, "is empty now".format(place[0], place[1]))
        for i in range(0,5):
            Parking_place.matrixx[2][i] = "empty"