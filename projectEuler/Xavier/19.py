import time
from math import sqrt

from utils import add_one, prime_numbers


def ndays(i, year):
    if i in [1,3,5,7,8,10,12] :
        return 31
    elif i in [4,6,9,11] :
        return 30
    elif i == 2:
        days = 28
        if year % 4 == 0 and year % 100 != 0:
            days = 29
        if year % 400 == 0 :
            days = 29
        return days
    else :
        return -800007

class Date:
    def __init__(self):
        self.mois = 1
        self.year = 1901
    def next(self):
        # incrementer le mois
        self.mois += 1
        if self.mois == 13:
            self.mois = 1
            self.year += 1


if __name__ == '__main__' :
    start = time.time()

    DaysListe = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

    cnt = 0
    day = 1
    date = Date()
    #print(date.mois, date.year, DaysListe[day])
    while date.year < 2001:
        day += ndays(date.mois, date.year) % 7
        day = day % 7
        date.next()
        #print(date.mois, date.year, DaysListe[day], cnt)
        
        # incrementer le mois
        if day == 6 :
            cnt += 1
            print(date.mois, date.year, DaysListe[day], cnt)
        

    print("Result: ", cnt)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
