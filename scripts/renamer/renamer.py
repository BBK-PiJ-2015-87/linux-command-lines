# 1. 2016_01_01_000_01-01-2016-Name_Surname_8000000
#
import re

file = '1-01-2016-Name_Surname_8000000'

def standardiseDate(date):
    if (date[1] == '-'):
        return '0' + date
    else:
        return date


print(standardiseDate('1-01-2016-Name_Surname_8000000'))
print(standardiseDate('01-01-2017-Name_Surname_8000000'))




