from booking import *


def main():
    random = Room.random()
    client_list = Room.reader('booking.txt')
    room_list = Room.reader('fund.txt')
    main_dict = {}
    for i in room_list:
        places = 0
        comfort = 0
        a, b, c, d = i.split()
        if c == '1':
            places = 2900
        elif c == '2':
            places = 2300
        elif c == '3':
            if b == 'полулюкс':
                places = 3200
            else:
                places = 4100
        if d == 'стандарт':
            comfort = 1.0
        elif d == 'стандарт_улучшенный':
            comfort = 1.2
        elif d == 'апартамент':
            comfort = 1.5
        e = Room.get_price(Room(places, comfort))
        main_dict[a] = [b, c, d, e]
    for i in main_dict.keys():
        main_dict[i].append(Booking(main_dict[i][3], 280))
        main_dict[i].append(Booking(main_dict[i][3], 1000))
        main_dict[i].append('свободен')
    print(main_dict)
    print(client_list)
    main_list = []
    for i in client_list:
        a,b,c,d,e,f,g,h = i.split()
        main_list += [[a,b,c,d,e,f,g,h]]
    print(main_list)
    list_room = []
    for i in main_dict.values():
        list_room += [i]
        
    '''list_room - список номеров с тремя значениями стоимости (в зависимости от питания)
        main_list - список посетителей'''

    # TODO: доработать
    if random == 1:
        print('Клиент отказался от варианта')
    else:
        print('Клиент согласен. Номер забронирован')


if __name__ == '__main__':
    main()
