"""
    @Author  : Piyus Gupta
    @email   : PiyusGupta01@gmail.com
    @created : Jan 02, 2024

    ProjectEuler Q-19 : How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

    ref : https://projecteuler.net/problem=19
"""
import sys
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31,
                 30, 31, 30, 31]  # will add leap year on feb
days_of_week = [0, 1, 2, 3, 4, 5, 6]  # considering 0 is Sunday


def is_a_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main():
    # starting from Jan 1, 1900 it's Monday
    counter = 0
    next_day = 2  # 1st jan 1901 is Tuesday
    for year in range(1901, 2001):
        for month, days in enumerate(days_in_month):
            if month == 1:
                next_day += 1 if is_a_leap_year(year) else 0
            next_day = (next_day + days) % 7
            if next_day == 0:
                counter += 1
    return counter


if __name__ == '__main__':
    print("Total sunday on day 1 : ", main())
