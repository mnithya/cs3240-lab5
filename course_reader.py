__author__ = 'nm3zr'

import csv

def load_course_database(db_name, csv_filename):
    with open(csv_filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            #print(row['deptID'], row['courseNum'], row['semester'], row['meetingType'], row['seatsTaken'], row['seatsOffered'], row['instructor'])
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
load_course_database('course1.db', 'seas-courses-5years.csv')