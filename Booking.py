import random
from .Flight import Flight
class Booking():
    def __init__(self, flight, type, status, user):
        self.id = random.random()
        self.flight = flight
        self.type = type
        self.status = status
        self.user = user
        