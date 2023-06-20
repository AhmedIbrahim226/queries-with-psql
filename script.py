from time import sleep

from utilities.jsonUrl import JsonUrl
from utilities.queries import obj


def inputs():
    print('Please Select Option: [1 or Databases], [2 or Search in databases], [3 or Import data from JSON URL]')
    in1 = input('Choose one of the previous options : ')

    while True:
        if in1 == '1' or in1 == 'Databases' or in1 == '2' or in1 == 'Search in databases' or in1 == '3' or in1 == 'Import data from JSON URL':
            break
        print('\n----Please Enter Valid Choice----')
        in1 = input('Choose one of the previous options : ')

    if in1 == '1' or in1 == 'Databases':
        print('\n\nSelect Option: [1 or All databases], [2 or Create database], [3 or Remove database]')
        in2 = input('Choose one of the previous options : ')

        if in2 == '1' or in2 == 'All databases':
            obj.getAllDatabase()

        elif in2 == '2' or in2 == 'Create database':
            dataName = input('Enter database name : ')
            obj.createDatabase(dataName)

        elif in2 == '3' or in2 == 'Remove database':
            dataName = input('Enter database name to remove : ')
            obj.removeDatabase(dataName)
        else:
            return print("error")

    if in1 == '2' or in1 == 'Search in databases':
        in3 = input('\n\nPlease enter your WORD to search : ')
        obj.searchInDatabase(in3)

    if in1 == '3' or in1 == 'Import data from JSON URL':
        sleep(2)
        print('Importing in progress.........')
        JsonUrl()


inputs()
