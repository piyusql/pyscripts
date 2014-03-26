#!/usr/bin/python

import sys
import csv
import random
import calendar

DEFAUTL_FROM_YEAR = 1995
DEFAULT_COMPANY_COUNT = 10

class SharePrice(object):
    """
        class is made for writing sample share data in csv,
        it also reads data from csv and define the duration when the share price was at its max for each company
    """
    def __init__(self, _company_count = DEFAULT_COMPANY_COUNT, _year_from = DEFAUTL_FROM_YEAR):
        self.company_count = _company_count
        self.year_from = _year_from
        self.header = []
        self.data = []

    def generate_sample_data(self):
        file_data = []
        header = ['Year', 'Month']
        header.extend(['Company-%d' %(c+1) for c in range(self.company_count)])
        self.header = header
        #iteration of year till 2013
        for _year in range(self.year_from, 2014):
            for _month in range(12):
                row_data = [_year, calendar.month_abbr[_month+1]]
                row_data.extend([random.randint(10,1000) for i in range(self.company_count)])
                file_data.append(row_data)
            #End for a year
        self.data = file_data

    def write_to_csv(self, file_path):
        with open(file_path, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.header)
            writer.writerows(self.data)
        return file_path

    def read_from_csv(self, file_path):
        data = []
        try:
            with open(file_path, 'rb') as csv_file:
                reader = csv.reader(csv_file)
                self.header = reader.next()
                for row in reader:
                    data.append(row)
            self.data = data
        except IOError as e:
            print e
            return

    def get_max_index(self):
        company_data = {}
        for row, each_row in enumerate(self.data):
            for column, key in enumerate(self.header):
                if key not in company_data:
                    company_data[key] = []
                company_data[key].append(self.data[row][column])
        result = {}
        for c in range(self.company_count):
            key = "Company-%d" %(c+1)
            value = company_data[key]
            max_indices = [i for i in range(len(value)) if value[i] == max(value)]
            #get the year from 0th index, month from 1st index
            durations = ["%s-%s" %(company_data['Year'][index], company_data['Month'][index]) for index in max_indices]
            result[key] = ", ".join(durations)
        return result

def main(args):
    print args
    if len(args)<2:
        print "\n\tplease follow the Usage instructions !!!"
        sys.exit(0)
    try:
        obj = SharePrice(int(args[2]) if len(args)>2 else DEFAULT_COMPANY_COUNT, int(args[3]) if len(args)>3 else DEFAUTL_FROM_YEAR)
    except ValueError as e:
        print "provided data is not valid, i m using a default values for demo"
        obj = SharePrice()
    obj.generate_sample_data()
    #write data to csv
    obj.write_to_csv(args[1])
    obj.read_from_csv(args[1])
    result = obj.get_max_index()
    for index in range(obj.company_count):
        key = 'Company-%d' %(index+1)
        print "%s at its max on %s" %(key, result.get(key, '-NA-'))
    print "\n\tyou can check the data from : %s" %(args[1])


if __name__ == '__main__':
    print "\n\tUsage : `python %s <file_name.csv> <company_count : default 10> <year_from : default 1990>`\n" %(sys.argv[0])
    main(sys.argv)
