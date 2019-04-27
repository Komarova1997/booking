import random


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
            if 'одноместный' in i:
                if 'стандарт' in i:
                    i.append(self.places[0]*self.comfort[0])
                if 'стандарт_улучшенный' in i:
                    i.append(self.places[0]*self.comfort[1])
                if 'апартамент' in i:
                    i.append(self.places[0]*self.comfort[2])
            if 'двухместный' in i:
                if 'стандарт' in i:
                    i.append(self.places[1]*self.comfort[0])
                if 'стандарт_улучшенный' in i:
                    i.append(self.places[1]*self.comfort[1])
                if 'апартамент' in i:
                    i.append(self.places[1]*self.comfort[2])
            if 'полулюкс' in i:
                if 'стандарт' in i:
                    i.append(self.places[2] * self.comfort[0])
                if 'стандарт_улучшенный' in i:
                    i.append(self.places[2] * self.comfort[1])
                if 'апартамент' in i:
                    i.append(self.places[2] * self.comfort[2])
            if 'люкс' in i:
                if 'стандарт' in i:
                    i.append(self.places[3] * self.comfort[0])
                if 'стандарт_улучшенный' in i:
                    i.append(self.places[3] * self.comfort[1])
                if 'апартамент' in i:
                    i.append(self.places[3] * self.comfort[2])
            list_room += [i]
        main_list = []
        for i in list_room:
            c = i.copy()
            d = i.copy()
            c[4] += 280.0
            c.append('завтрак')
            d[4] += 1000.0
            d.append('полупансион')
            i.append('без питания')
            main_list += [[i, c, d, ['*']*31]]
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
