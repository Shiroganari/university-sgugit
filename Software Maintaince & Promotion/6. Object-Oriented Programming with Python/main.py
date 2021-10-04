import datetime


class AirTicketOffice:
    flights = []

    # Создание нового рейса
    def new_flight(self, flight_number, airplane_type,
                   departure_year, departure_month, departure_day, departure_hour, departure_minute, free_spots, price):
        self.flights.append(Flights(flight_number, airplane_type,
                                    departure_year, departure_month, departure_day, departure_hour, departure_minute,
                                    free_spots, price))

    # Поиск нужного рейса по цене
    def find_flight_by_price(self):
        print("Введите максимальную цену: ")
        max_price = int(input())
        is_exist = False

        for flight in self.flights:
            if flight.price < max_price:
                is_exist = True

        if is_exist:
            print("Список рейсов, стоимость на билеты которых не превышает ", max_price, " рублей.")
        else:
            print("Нет подходящих рейсов.")
            return

        for flight in self.flights:
            if flight.price < max_price:
                print("Номер рейса: ", flight.flight_number)
                print("Дата вылета: ", flight.departure_date.strftime("%A, %d. %B %Y"))
                print("Количество свободных мест: ", flight.free_spots)
                print("Стоимость билета: ", flight.price)

    # Поиск нужного рейса по дате
    def find_flight_by_date(self):
        print("Поиск рейса по дате")

        print("Введите год: ")
        departure_year = int(input())
        print("Введите месяц: ")
        departure_month = int(input())
        print("Введите день: ")
        departure_day = int(input())

        departure = datetime.date(departure_year, departure_month, departure_day)

        is_exist = False

        for flight in self.flights:
            if departure == flight.departure_date:
                is_exist = True

        if is_exist:
            print("Список рейсов, которые отправляются: ", departure.strftime("%A, %d. %B %Y"))
        else:
            print("Нет подходящих рейсов.")
            return

        for flight in self.flights:
            if departure == flight.departure_date:
                print("Номер рейса: ", flight.flight_number)
                print("Дата вылета: ", flight.departure_date.strftime("%A, %d. %B %Y"))
                print("Количество свободных мест: ", flight.free_spots)
                print("Стоимость билета: ", flight.price, " РУБ.")
                print()


class Flights:
    def __init__(self, flight_number, airplane_type,
                 departure_year, departure_month, departure_day, departure_hour, departure_minute, free_spots, price):
        self.flight_number = flight_number
        self.airplane_type = airplane_type
        self.departure_date = datetime.date(departure_year, departure_month, departure_day)
        self.departure_time = datetime.datetime(departure_year, departure_month, departure_day,
                                                departure_hour, departure_minute)
        self.free_spots = free_spots
        self.price = price


ATO = AirTicketOffice()

ATO.new_flight(5, "Airbus A330", 2021, 9, 1, 17, 30, 20, 3000)
ATO.new_flight(23, "Being-737", 2021, 12, 1, 17, 30, 20, 5000)

ATO.find_flight_by_price()