import random
import ru_local


class Room:
    places = [2900, 2300, 3200, 4100]
    comfort = [1.0, 1.2, 1.5]

    def __init__(self):
        super(Room, self).__init__(places=Room.places,
                                   comfort=Room.comfort)

    def booking_variants(self):
        room_list = Room.reader('fund.txt')
        list_room = []
        for i in room_list:
            i = i.split()
            if ru_local.ONE in i:
                if ru_local.STANDARD in i:
                    i.append(self.places[0]*self.comfort[0])
                if ru_local.STANDARD_IMPROVED in i:
                    i.append(self.places[0]*self.comfort[1])
                if ru_local.APARTMENT in i:
                    i.append(self.places[0]*self.comfort[2])
            if ru_local.TWO in i:
                if ru_local.STANDARD in i:
                    i.append(self.places[1]*self.comfort[0])
                if ru_local.STANDARD_IMPROVED in i:
                    i.append(self.places[1]*self.comfort[1])
                if ru_local.APARTMENT in i:
                    i.append(self.places[1]*self.comfort[2])
            if ru_local.HALF_LUX in i:
                if ru_local.STANDARD in i:
                    i.append(self.places[2] * self.comfort[0])
                if ru_local.STANDARD_IMPROVED in i:
                    i.append(self.places[2] * self.comfort[1])
                if ru_local.APARTMENT in i:
                    i.append(self.places[2] * self.comfort[2])
            if ru_local.LUX in i:
                if ru_local.STANDARD in i:
                    i.append(self.places[3] * self.comfort[0])
                if ru_local.STANDARD_IMPROVED in i:
                    i.append(self.places[3] * self.comfort[1])
                if ru_local.APARTMENT in i:
                    i.append(self.places[3] * self.comfort[2])
            list_room += [i]
        main_list = []
        for i in list_room:
            c = i.copy()
            d = i.copy()
            c[4] += 280.0
            c.append(ru_local.BREAKFAST)
            d[4] += 1000.0
            d.append(ru_local.HALF_BOARD)
            i.append(ru_local.NO_FOOD)
            main_list += [[i, c, d, '*'*31]]
        return main_list

    @staticmethod
    def reader(file):
        main_list = []
        with open(file, 'r') as f:
            for i in f.readlines():
                main_list += [i]
        return main_list

    @staticmethod
    def random():
        main_list = [1, 2, 3, 4]
        answer = random.choice(main_list)
        return answer
