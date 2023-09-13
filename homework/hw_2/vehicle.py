from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, company, model, yearRelease, numWheels, speed):
        self.company = company
        self.model = model
        self.yearRelease = yearRelease
        self.numWheels = numWheels
        self.speed = speed

    @abstractmethod
    def testDrive(self):
        pass

    @abstractmethod
    def park(self):
        pass


class Car(Vehicle):

    def __init__(self, company, model, yearRelease):
        self.company = company
        self.model = model
        self.yearRelease = yearRelease
        self._numWheels = 4
        self._speed = 0

    def testDrive(self):
        self._speed = 60

    def park(self):
        self._speed = 0

    @property
    def get_numwheels(self):
        return self._numWheels
    @property
    def get_speed(self):
        return self._speed


class Motorcycle(Vehicle):
    def __init__(self, company, model, yearRelease):
        self.company = company
        self.model = model
        self.yearRelease = yearRelease
        self._numWheels = 2
        self._speed = 0

    def testDrive(self):
        self._speed = 75

    def park(self):
        self._speed = 0

    @property
    def get_numwheels(self):
        return self._numWheels

    @property
    def get_speed(self):
        return self._speed
