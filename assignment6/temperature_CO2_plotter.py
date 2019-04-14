#!/usr/bin/env python3
import matplotlib.pyplot as plt

# a program tat produces an png based on arguments of what time frame to look in and uses data in csv files

def plot_temperature(month, yearFrom, yearTo, m=0, ma=0):
    """ Function that plots temperatures of a given year.
    saves an png file with the corresponding graph

    Args:
        month   (int) : the month ..
        yearFrom (int) : year from what to display
        yearTo (int) : year to graph for display
        m (int) : minium y axis
        ma (int) : max value y axis

    Returns:
        none

    """

    # opens file for reading
    fil=open("temperature.csv", "r+")
    # reads file
    # print(fil.read()    )
    plt.title('Temperature vs history')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    if m!=ma:
        plt.ylim((m, ma))
    # plt.axis()
    # plt.grid(True)
    counter=0
    temp=[]
    year=[]

    for n in fil:
        if counter!=0:
            data=n.split(",")
            # pyploy plt
            if int(data[0])>=yearFrom and float(data[0])<=yearTo:
                # print(data[0])
                # print(data[month])
                temp.append(float(data[month]))
                year.append(int(data[0]))

        else:
            counter+=1
        # separates file year by year
        # print(n)

    plt.plot(year, temp)

    plt.savefig("static/Temperature.png")
    plt.clf()

def plot_CO2(yearFrom, yearTo, m=0, ma=0):
    """ Function that plots temperatures of a given year.
    saves an png file with the corresponding graph

    Args:
        yearFrom (int) : year from what to display
        yearTo (int) : year to graph for display
        m (int) : minium y axis
        ma (int) : max value y axis

    Returns:
        none
    """

    fil=open("co2.csv", "r")
    # reads file
    # print(fil.read()    )
    plt.title('CO2 vs history')
    plt.xlabel('Date')
    plt.ylabel('CO2')
    if m!=ma:
        plt.ylim((m, ma))
    # plt.axis()
    # plt.grid(True)
    counter=0
    temp=[]
    year=[]

    for n in fil:
        if counter!=0:
            data=n.split(",")
            # pyploy plt
            if int(data[0])>=yearFrom and float(data[0])<=yearTo:
                # print(data[0])
                # print(data[month])
                temp.append(float(data[1]))
                year.append(int(data[0]))

        else:
            counter+=1
        # separates file year by year
        # print(n)

    plt.plot(year, temp)

    plt.savefig("static/CO2.png")
    plt.clf()


# month, yearFrom, yearTo, min, max
# plot_temperature(1, 1970, 2011, -5, 1)
# plot_CO2(1, 1970, 2011)
