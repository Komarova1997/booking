from booking import *


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
        print('Поступила заявка на бронирование:')
        print()
        print(client_list[list_1.index(client)])
        print()
        variants = []
        places = []
        for room in fund_list:
            # проверка занятости по дате и по указаной клиентом цене
            if '#' not in room[3][client[5]-1:client[5]-1 + client[6]]:
                if room[0][4] <= client[-1]:
                    variants += [room[0]]
                if room[1][4] <= client[-1]:
                    variants += [room[1]]
                if room[2][4] <= client[-1]:
                    variants += [room[2]]
            # подбор вариантов по количеству мест
            for variant in variants:
                if int(variant[2]) == client[4]:
                    if variant not in places:
                        places += [variant]
                if int(variant[2]) >= client[4]:
                    if variant not in places:
                        places += [variant]
        # сортировка списка по наибольшей цене
        places = sorted(places, key=lambda place: place[4], reverse=True)
        # варианты размещения по максимальной цене
        if places != []:
            if int(places[0][2]) == client[4]:
                print('Найден:')
                print()
                print('номер ' + places[0][0] + ' ' +
                      places[0][1] + ' ' +
                      places[0][3] + ' расчитан на ' +
                      str(places[0][2]) + ' ' + 'чел. ' +
                      'фактически ' + str(client[4]) + ' ' + 'чел. ' +
                      places[0][-1] + ' ' + 'стоимость ' +
                      str(places[0][4]) + ' ' + 'руб./сутки')
                print()
                category = places[0][1]
                if category == 'одноместный':
                    single += 1
                if category == 'двухместный':
                    double += 1
                if category == 'полулюкс':
                    junior_suite += 1
                else:
                    lux += 1
                if Room.random() != 1:
                    print('Клиент согласен. Номер забронирован.')
                    count_room += 1
                    income += float(list_1[0][-1])
                    for room in fund_list:
                        if places[0] in room:
                            room[3] = room[3][:client[5]-1] + '#'*client[6] + room[3][client[5]+client[6]-1:]
                else:
                    print('Клиент отказался от варианта.')
                    lost_income += client[-1]
                    count_free_room += 1
            else:
                print('Найден:')
                print()
                print('номер ' + places[0][0] + ' ' +
                      places[0][1] + ' ' +
                      places[0][3] + ' расчитан на ' +
                      str(places[0][2]) + ' ' + 'чел. ' +
                      'фактически ' + str(client[4]) + ' ' + 'чел. ' +
                      places[0][-1] + ' ' + 'стоимость ' +
                      str(places[0][4] * 0.7) + ' ' + 'руб./сутки')
                print()
                category = places[0][1]
                if category == 'одноместный':
                    single += 1
                if category == 'двухместный':
                    double += 1
                if category == 'полулюкс':
                    junior_suite += 1
                if Room.random() != 1:
                    print('Клиент согласен. Номер забронирован.')
                    count_room += 1
                    income += float(list_1[0][-1])
                    for room in fund_list:
                        if places[0] in room:
                            room[3] = room[3][:client[5] - 1] + '#' * client[6] + room[3][client[5] + client[6] - 1:]
                else:
                    print('Клиент отказался от варианта.')
                    lost_income += client[-1]
                    count_free_room += 1
        else:
            print('Предложений по данному запросу нет. В бронировании отказано.')
            lost_income += client[-1]
            count_free_room += 1
        percent = (100 * count_room) / 24
        print()
        print('------------------------------------------------------------------------------------------------')
        print()
        try:
            if client[0] != list_1[list_1.index(client) + 1][0]:
                print()
                print('Итог за ' + client[0])
                print('Количество занятых номеров: ', count_room)
                print('Количество свободных номеров: ', count_free_room)
                print('Занятость по категориям:')
                print('Одноместных: ', single, ' из 9')
                print('Двухместных: ', double, ' из 6')
                print('Полулюкс: ', junior_suite, ' из 4')
                print('Люкс: ', lux, ' из 5')
                print('Процент загруженности гостиницы: ', percent, '%')
                print('Доход за день: ', income, ' руб.')
                print('Упущенный доход: ', lost_income, ' руб.')
                count_room = 0
                count_free_room = 0
                income = 0
                lost_income = 0
                single = 0
                double = 0
                junior_suite = 0
                lux = 0
        except IndexError:
            print()
            print('Итог за ' + client[0])
            print('Количество занятых номеров: ', count_room)
            print('Количество свободных номеров: ', count_free_room)
            print('Занятость по категориям:')
            print('Одноместных: ', single, ' из 9')
            print('Двухместных: ', double, ' из 6')
            print('Полулюкс: ', junior_suite, ' из 4')
            print('Люкс: ', lux, ' из 5')
            print('Процент загруженности гостиницы: ', percent, '%')
            print('Доход за день: ', income, ' руб.')
            print('Упущенный доход: ', lost_income, ' руб.')
# TODO: отчет по каждому дню доредактирвоать


if __name__ == '__main__':
    main()
