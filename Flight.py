# Talha Chaudhry
# tchaud@uwo.ca
# November 28, 2022
# Assignment 4 (Air Travel)

from Airport import *  # imports all functions from Airport.py


class Flight:

    # ! FUNCTIONS !

    def __init__(self, flightNo, origin, destiniation):  # initializes object
        if isinstance(origin, Airport) and isinstance(destiniation, Airport):  # checks if origin and destination are
            self._flightNo = flightNo  # airport objects
            self._origin = origin
            self._destination = destiniation

        else:  # raises TypeError if origin and destination are not airport objects
            raise TypeError("the origin and destination must be airport objects")

    def __repr__(self):  # returns string that contains flightNo, origin, destination and flightType
        if self._origin.getCountry() == self._destination.getCountry():
            flightType = "{domestic}"  # if origin country is same as destination country, flightType is domestic
        else:  # if not, flight is international
            flightType = "{international}"

        return "Flight: {} from {} to {} {}".format(self._flightNo, self._origin.getCity(), self._destination.getCity(),
                                                    flightType)

    def __eq__(self, other):  # checks if 2 flight objects have equal origins and destination
        if isinstance(other, Flight):
            if other._destination == self._destination and other._origin == self._origin:
                return True
            else:  # returns false if other is not a flight object
                return False
        else:  # returns false if flights are not equal
            return False

    def isDomesticFlight(self):  # checks if implicit object is a domestic flight
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False

    # ! GETTER FUNCTIONS !

    def getFlightNumber(self):  # returns flightNumber of implicit object
        return self._flightNo

    def getOrigin(self):  # returns origin airport of implicit object
        return self._origin

    def getDestination(self):  # returns destination airport of implicit object
        return self._destination

    # ! SETTER FUNCTIONS !

    def setOrigin(self, origin):  # sets origin of implicit object to parameter
        self._origin = origin

    def setDestination(self, destination):  # sets destination of implicit object to parameter
        self._destination = destination
