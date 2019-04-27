from booking import *


def main():
    fund_list = Room.booking_variants(Room)
    client_list = Room.reader('booking.txt')
    list_1 = []
    for i in client_list:
        client_list[client_list.index(i)] = i[:-1]
        a, b, c, d, e, f, g, h = i.split()
        list_1 += [[a, b, c, d, int(e), f, int(g), float(h)]]
    print(fund_list)
    variants = []
    main_list = []
    for client in list_1:
        for room in fund_list:
            if room[0][4] <= client[-1]:
                variants += [room[0]]
            if room[1][4] <= client[-1]:
                variants += [room[1]]
            if room[2][4] <= client[-1]:
                variants += [room[2]]
        main_list += [[client, variants]]
        variants = []
    print(main_list)


if __name__ == '__main__':
    main()
