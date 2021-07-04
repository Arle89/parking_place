class Parking_place():
    def __init__(self):
        self.small = small = ['empty','empty','empty','empty','empty']
        self.medium = medium = ['empty','empty','empty','empty','empty']
        self.big = big = ['empty','empty','empty','empty','empty']
        self.matrix = matrix = [small,
                                medium,
                                big]
    
    def display_parking(self):
        for i in self.matrix:
            print(i)


class Moto(Parking_place):
    def __init__(self):
        self.size = size = 1
        self.park_place = park_place = Parking_place.matrix
    
    def parking(self):
        for i in self.park_place:
            for j in i:
                if j == "empty":
                    print(i.index(j))
                    j = "moto"
                else:
                    print("Parking is busy")
        print(Parking_place.display_parking)

class Avto(Parking_place):
    def __init__(self):
        self.size = size = 1


x = Parking_place()
x.display_parking()
y = Moto()
y.parking