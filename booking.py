import random


class Room:
    '''Класс номеров
    (places - количество мест в номере,
    comfort - степень комфорта,
    price - стоимость номера)'''
    def __init__(self, places, comfort):
        self._places = places
        self._comfort = comfort
        self._price = places * comfort

    def __str__(self):
        return self._price

    def __repr__(self):
        return self.__str__()

    def get_price(self):
        return self._price

    @staticmethod
    def random():
        main_list = [1, 2, 3, 4]
        answer = random.choice(main_list)
        return answer

    @staticmethod
    def reader(file):
        main_list = []
        with open(file, 'r') as f:
            for i in f.readlines():
                main_list += [i[:-1]]
        return main_list

    @staticmethod
    def price_for_client(my_list, my_number):
        return min(my_list, key=lambda x: abs(x - my_number))

class Booking():
    '''Класс размещения
    (Информация о номере и о питании)'''
    def __init__(self, _price, food):
        self._food = food
        self._main_price = _price + food

    def __str__(self):
        return str(self._main_price)

    def __repr__(self):
        return self.__str__()

    def get_main_price(self):
        return self._main_price
