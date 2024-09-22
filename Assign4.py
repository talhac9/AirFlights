# Talha Chaudhry
# tchaud@uwo.ca
# November 28, 2022
# Assignment 4 (Air Travel)

from Airport import *  # imports all functions from Airport.py
from Flight import *  # imports all functions from Flights.py

allAirports = []  # a list that stores data for airports file
allFlights = {}  # a dictionary that stores data for flights file


def loadData(airportFile, flightFile):
    try:
        f = open(airportFile, "r", encoding='utf8')  # opens airport file for reading
        f2 = open(flightFile, "r", encoding='utf8')  # opens flight file for reading
        flightList = []  # empty container to store all flights in

        for line in f:
            entries = line.split(",")  # splits every entry before "," into a list called entries as an element

            # stores airport data from file and removes all whitespace from left and right side of string
            allAirports.append(Airport(entries[0].strip(), entries[2].strip(), entries[1].strip()))

        for line in f2:
            entries = line.split(",")  # splits every entry before "," into a list called entries as an element

            # gets data from flights file and checks to see if origin and destination are aiport objects
            for i in range(len(allAirports)):
                if allAirports[i].getCode() == entries[1].strip():
                    origin = i
                if allAirports[i].getCode() == entries[2].strip():
                    destination = i

            # appends flight object to flightList
            flightList.append(Flight(entries[0].strip(), allAirports[origin], allAirports[destination]))

            allFlights[entries[1].strip()] = []  # creates all the keys in dictionary using origin airport code

        for key in allFlights.keys():  # adds values in dictionary by looping through
            for i in range(len(flightList)):  # each key in allFlights and element in flightList
                if key == flightList[i].getOrigin().getCode():
                    allFlights[key].append(flightList[i])

        f.close()  # closes airport file
        f2.close()  # closes flights file

        return allAirports, allFlights  # returns data to empty containers initialized outside of function

    except FileNotFoundError:  # if invalid file is inputted, will print and return false
        print("file not found")
        return False


def getAirportByCode(code):  # Returns the Airport object that has the given code
    for i in range(len(allAirports)):  # loops trough allAirports

        if code.lower() == allAirports[i].getCode().lower():  # if code is a code for an object in allAirports,
            airport = allAirports[i]  # returns the airport object and if not returns -1
            break

        else:
            airport = -1

    return airport


def findAllCityFlights(city):  # Return a list that contains all Flight objects that involve the given city

    listOfFlights = []  # creates a container called listOfFlights, will contain all flights that equal city

    for keys in allFlights.keys():  # loops through each key in allFlights and its values
        for x in range(len(allFlights[keys])):

            if allFlights[keys][x].getOrigin().getCity().lower() == city.lower():
                listOfFlights.append(allFlights[keys][x])  # if origin contains city, appends to listOfFlights

            if allFlights[keys][x].getDestination().getCity().lower() == city.lower():
                listOfFlights.append(allFlights[keys][x])  # if destination contains city, appends to listOfFlights

    return listOfFlights  # returns listOfFlights as a list


def findAllCountryFlights(country):  # Returns a list that contains all Flight objects that involve the given country
    listOfFlights = []  # creates a container called listOfFlights, will contain all flights that equal country

    for keys in allFlights.keys():  # loops through each key in allFlights and its value
        for x in range(len(allFlights[keys])):

            if allFlights[keys][x].getOrigin().getCountry().lower() == country.lower():
                listOfFlights.append(allFlights[keys][x])  # if origin contains country, appends to listOfFlights

            elif allFlights[keys][x].getDestination().getCountry().lower() == country.lower():
                listOfFlights.append(allFlights[keys][x])  # if destination contains country, appends to listOfFlights

            elif allFlights[keys][x].getOrigin().getCountry().lower() == country.lower() and \
                    allFlights[keys][x].getDestination().getCountry().lower() == country.lower():
                listOfFlights.append(allFlights[keys][x])
                # if destination or origin contain country, appends to listOfFlights

    return listOfFlights  # returns listOfFlights as a list


def findFlightBetween(origAirport, destAirport):
    # check if there is a single-hop connecting flight from origAirport to destAirport.

    connectedFlights = set()  # empty set that will store connected flights
    possibleConnect = []  # empty list that will store possible 1 layover connected flights

    for keys in allFlights.keys():  # Checks if there is a direct flight from origAirport to destAirport
        for x in range(len(allFlights[keys])):

            if allFlights[keys][x].getOrigin() == origAirport and allFlights[keys][x].getDestination() == destAirport:
                return "Direct Flight: {} to {}".format(origAirport.getCode(), destAirport.getCode())

            if allFlights[keys][x].getOrigin() == origAirport:  # appends all airports with same origin to
                possibleConnect.append(allFlights[keys][x])     # possibleConnect

    for i in possibleConnect:
        destination = i.getDestination()  # gets destination of each flight in possibleConnect

        for keys in allFlights.keys():    # loops through keys and values
            for x in range(len(allFlights[keys])):

                # checks if destination is equal to origin and destAirport is equal to a destination from dictionary
                if allFlights[keys][x].getOrigin() == destination and allFlights[keys][x].getDestination() == destAirport:
                    connectedFlights.add(allFlights[keys][x].getOrigin().getCode())  # adds to connectedFlights set

    if connectedFlights == set():  # if set is empty, returns -1
        return -1

    else:
        return connectedFlights


def findReturnFlight(firstFlight):  # returns flight object that goes opposite direction of flight in parameter

    for keys in allFlights.keys():  # loops through each key in allFlights and its values
        for x in range(len(allFlights[keys])):

            if allFlights[keys][x].getOrigin() == firstFlight.getDestination() and \
                    allFlights[keys][x].getDestination() == firstFlight.getOrigin():
                # finds flight with opposite route of firstFlight and returns the flight object
                return allFlights[keys][x]

    return -1  # if no opposite flight found, returns -1
