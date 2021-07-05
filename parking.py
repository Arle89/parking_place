

class Parking_place():
        small = ['empty','empty','empty','empty','empty']
        medium = ['empty','empty','empty','empty','empty']
        big = ['empty','empty','empty','empty','empty']
        matrixx = [small,
                medium,
                big]
        def display_parking(self):
            for i in self.matrixx:
                print(i)
        
        def park_proces(self, vtype):
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
                print("Sorry, we has no place for your vehicle")




class Moto(Parking_place):
    park_place = Parking_place.matrixx

    def park_proces(self):
        for i in range(0,3):
            for j in range(0,5):
                if self.park_place[i][j] == "empty":
                    self.park_place [i][j] = "moto"
                    #self.park_place[j].insert(self.park_place[i,j].index("empty"), "moto")
                break
            break


class Avto(Parking_place):
    park_place = Parking_place.matrixx

    def park_proces(self):
        for i in range(1,3):
            for j in range(0,5):
                if self.park_place[i][j] == "empty":
                    self.park_place[i][j] = "avto"
                break
            break


class Bus(Parking_place):
    park_place = Parking_place.matrixx

    def park_proces(self):
        for i in self.park_place[2]:
            if i == "empty":
                self.park_place[2] = r"bus"
                break
            break


x = Parking_place()
x.display_parking()
x.park_proces("moto")
x.display_parking()
x.park_proces("avto")
x.park_proces("avto")
x.park_proces("bus")
x.display_parking()