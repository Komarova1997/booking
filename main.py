from booking import *
import ru_local


def main():
    fund_list = Room.booking_variants(Room)
    client_list = Room.reader('booking.txt')
    list_1 = []
    for i in client_list:
        client_list[client_list.index(i)] = i[:-1]
        a, b, c, d, e, f, g, h = i.split()
        list_1 += [[a, b, c, d, int(e), int(f[:2]), int(g), float(h)]]

    count_room = 0
    count_free_room = 0
    income = 0
    lost_income = 0
    single = 0
    double = 0
    junior_suite = 0
    lux = 0
    for client in list_1:
        print(ru_local.RESERVATION_REQUEST_RECEIVED)
        print()
        print(client_list[list_1.index(client)])
        print()
        variants = []
        places = []
        for room in fund_list:
            # verification of employment by the date and the price specified by the client
            if '#' not in room[3][client[5]-1:client[5]-1 + client[6]]:
                if room[0][4] <= client[-1]:
                    variants += [room[0]]
                if room[1][4] <= client[-1]:
                    variants += [room[1]]
                if room[2][4] <= client[-1]:
                    variants += [room[2]]
            # selection of variants for the number of seats
            for variant in variants:
                if int(variant[2]) == client[4]:
                    if variant not in places:
                        places += [variant]
                if int(variant[2]) >= client[4]:
                    if variant not in places:
                        places += [variant]
        # sorting the list at the highest price
        places = sorted(places, key=lambda place: place[4], reverse=True)
        # accommodation options at the highest price
        if places != []:
            if int(places[0][2]) == client[4]:
                print(ru_local.FOUND)
                print()
                print(ru_local.ROOM + places[0][0] + ' ' +
                      places[0][1] + ' ' +
                      places[0][3] + ru_local.FOR +
                      str(places[0][2]) + ' ' + ru_local.PEOPLE +
                      ru_local.IN_FACT + str(client[4]) + ' ' + ru_local.PEOPLE +
                      places[0][-1] + ' ' + ru_local.PRISE +
                      str(places[0][4]) + ' ' + ru_local.RUB)
                print()
                category = places[0][1]
                if Room.random() != 1:
                    print(ru_local.CLIENT_AGREE)
                    count_room += 1
                    income += round(float(places[0][4]), 2)
                    for room in fund_list:
                        if places[0] in room:
                            room[3] = room[3][:client[5]-1] + '#'*client[6] + room[3][client[5]+client[6]-1:]
                            if category == ru_local.ONE:
                                single += 1
                            if category == ru_local.TWO:
                                double += 1
                            if category == ru_local.HALF_LUX:
                                junior_suite += 1
                            if category == ru_local.LUX:
                                lux += 1
                else:
                    print(ru_local.CLIENT_REFUSED)
                    lost_income += round(float(places[0][4]), 2)
            else:
                print(ru_local.FOUND)
                print()
                print(ru_local.ROOM + places[0][0] + ' ' +
                      places[0][1] + ' ' +
                      places[0][3] + ru_local.FOR +
                      str(places[0][2]) + ' ' + ru_local.PEOPLE +
                      ru_local.IN_FACT + str(client[4]) + ' ' + ru_local.PEOPLE +
                      places[0][-1] + ' ' + ru_local.PRISE +
                      str(places[0][4] * 0.7) + ' ' + ru_local.RUB)
                print()
                category = places[0][1]
                if Room.random() != 1:
                    print(ru_local.CLIENT_AGREE)
                    count_room += 1
                    income += float(list_1[0][-1])
                    for room in fund_list:
                        if places[0] in room:
                            room[3] = room[3][:client[5] - 1] + '#' * client[6] + room[3][client[5] + client[6] - 1:]
                            if category == ru_local.ONE:
                                single += 1
                            if category == ru_local.TWO:
                                double += 1
                            if category == ru_local.HALF_LUX:
                                junior_suite += 1
                            if category == ru_local.LUX:
                                lux += 1
                else:
                    print(ru_local.CLIENT_REFUSED)
                    lost_income += round(float(places[0][4]), 2)
                    count_free_room += 1
        else:
            print(ru_local.NO_OFFERS)
            lost_income += client[-1]
        count_free_room = 24 - count_room
        percent = round(((100 * count_room) / 24), 2)
        print()
        try:
            if client[0] == list_1[list_1.index(client) + 1][0]:
                print('------------------------------------------------------------------------------------------------')
                print()
        except IndexError:
            print('------------------------------------------------------------------------------------------------')
            print()
        try:
            if client[0] != list_1[list_1.index(client) + 1][0]:
                print('================================================================================================')
                print()
                print(ru_local.TOTAL + client[0])
                print(ru_local.NUMBER_OF_OCCUPIED_ROOMS, count_room)
                print(ru_local.NUMBER_OF_FREE_ROOMS, count_free_room)
                print(ru_local.EMPLOYMENT_BY_CATEGORY)
                print(ru_local.FOR_ONE, single, ru_local.FROM_9)
                print(ru_local.FOR_TWO, double, ru_local.FROM_6)
                print(ru_local.HALF_LUXX, junior_suite, ru_local.FROM_4)
                print(ru_local.LUXX, lux, ru_local.FROM_5)
                print(ru_local.PERCENT_OF_HOTEL_LOADING, percent, '%')
                print(ru_local.DAY_INCOME, income, ru_local.RUBL)
                print(ru_local.DAY_LOST_INCOME, lost_income, ru_local.RUBL)
                count_room = 0
                count_free_room = 0
                income = 0
                lost_income = 0
                single = 0
                double = 0
                junior_suite = 0
                lux = 0
        except IndexError:
            print('================================================================================================')
            print()
            print(ru_local.TOTAL + client[0])
            print(ru_local.NUMBER_OF_OCCUPIED_ROOMS, count_room)
            print(ru_local.NUMBER_OF_FREE_ROOMS, count_free_room)
            print(ru_local.EMPLOYMENT_BY_CATEGORY)
            print(ru_local.FOR_ONE, single, ru_local.FROM_9)
            print(ru_local.FOR_TWO, double, ru_local.FROM_6)
            print(ru_local.HALF_LUXX, junior_suite, ru_local.FROM_4)
            print(ru_local.LUXX, lux, ru_local.FROM_5)
            print(ru_local.PERCENT_OF_HOTEL_LOADING, percent, '%')
            print(ru_local.DAY_INCOME, income, ru_local.RUBL)
            print(ru_local.DAY_LOST_INCOME, lost_income, ru_local.RUBL)
            print()

if __name__ == '__main__':
    main()
