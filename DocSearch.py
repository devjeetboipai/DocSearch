
from enum import unique
from re import search
import string
import numpy as np


def search_function():
    result = []
    file_txt = open("Search.txt","r")
    for line in file_txt:
        line = line.strip()
        words = line.split(' ')
        for f in words:
            if(f.__contains__('RL50')):
                result.append(f)

    x = np.array(result)
    unique_list = np.unique(x)
    print(unique_list)
    print('===============================Staring Filteration=================================')
    trimmed_list = []
    for trim in unique_list:
        index_under = trim.rfind('_')
        index_full = trim.find('.') 
        if index_under != None and index_under != 4:
            index=index_under
        else:
            index = index_full
        #print(trim + 'Resultant = ' + trim[0:trim.find('.')])
        if(index!=-1):
            str = trim[0:index]
        else:
            str = trim
        #print(str + '==============Resultant =========== ' +trim )
        #print(index)
        trimmed_list.append(str)
        #print(str)
        for trim in trimmed_list:
            index_under = trim.rfind('_')
        index_full = trim.find('.') 
        if index_under != None and index_under != 4:
            index=index_under
        else:
            index = index_full
        #print(trim + 'Resultant = ' + trim[0:trim.find('.')])
        if(index!=-1):
            str = trim[0:index]
        else:
            str = trim
        #print(str + '==============Resultant =========== ' +trim )
        #print(index)
        print(str)
    file_txt.close()



if __name__ == '__main__':
    search_function()
