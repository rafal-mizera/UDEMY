import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert len(self.title) > 0,"Title is empty!"
        assert self.start <= self.end,"Start date is later than end date!"


    @classmethod
    def publish_offer(cls,trips):

        list_of_errorrs = []

        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errorrs.append(f"<{trip.symbol}>:<{e}>")
            except Exception as e:
                list_of_errorrs.append(f"<{trip.symbol}>:<{e}>")

        assert len(list_of_errorrs) == 0,f"The list of trips has errors: {list_of_errorrs}"

        print("The offer can be published")





trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]


try:
    print("Checking offer in progress...")
    Trip.publish_offer(trips)
    print("DONE...")
except Exception as e:
    print(f"An error has occured: {e}")


