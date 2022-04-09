from abc import ABC, abstractmethod


class ParkingSpot(ABC):
    def __init__(self, id, reserve):
        self.id = id
        self.reserve = reserve

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_reserve(self):
        pass


class HandicappedSPot(ParkingSpot):

    def get_id(self):
        return self.id

    def get_reserve(self):
        self.reserve


class CompactSPot(ParkingSpot):

    def get_id(self):
        return self.id

    def get_reserve(self):
        self.reserve


class LargeSPot(ParkingSpot):

    def get_id(self):
        return self.id

    def get_reserve(self):
        self.reserve


class BikeSPot(ParkingSpot):

    def get_id(self):
        return self.id

    def get_reserve(self):
        self.reserve

print(BikeSPot(1,True).get_id())  # 1


class ParkingTicket:
    def __init__(self, ticket_id, parking_spot_id, parking_spot_type, enter_time):
        self.ticket_id = ticket_id


class Terminal(ABC):


class EntryTerminal(Terminal):

    def get_ticket(self, parking_spot_type):
        pass

class ExitTerminal(Terminal):

    def accept_ticket(self, ticket):
        pass


class ParkingAssignmentStratergy:

