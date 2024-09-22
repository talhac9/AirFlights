# Talha Chaudhry
# tchaud@uwo.ca
# November 28, 2022
# Assignment 4 (Air Travel)

class Airport:

    # ! FUNCTIONS !

    def __init__(self, code, city, country):  # initializes an airport object with parameters passed in
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):  # returns a string that contains the code, city and country of implicit object
        return "{} ({}, {})".format(self._code, self._city, self._country)

    # ! GETTER FUNCTIONS !

    def getCode(self):  # returns code of implicit object
        return self._code

    def getCity(self):  # returns code of implicit object
        return self._city

    def getCountry(self):  # returns country of implicit object
        return self._country

    # ! SETTER FUNCTIONS !

    def setCity(self, city: str):  # sets city of implicit object to parameter
        self._city = city

    def setCountry(self, country: str):  # sets country of implicit object to parameter
        self._country = country
