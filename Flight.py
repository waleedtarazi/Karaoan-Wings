import random

class Flight():
    def __init__(self, departure, destination, number_of_seats):
        self.departure = departure
        self.destination = destination
        self.number_of_seats = number_of_seats
        self.id = random.random()