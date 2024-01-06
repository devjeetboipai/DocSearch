
from enum import unique
import os
from re import search
import string
import threading
from typing import final
from unittest import result
from urllib import response
import numpy as np

import time


def pause(massage = '\n Press any key to continue..............'):  # this function will pause the script with a default massage or a custome one.
    print(massage)
    os.system('pause >NULL')  # this will pause untill any key is pressed.
    return 0


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


def list_filteration(unique_list):
        resultset = []
        for trim in unique_list:
            index_under = trim.rfind('_')
        index_full = trim.find('.') 
        if index_under != None and index_under != 4:
            index=index_under
        else:
            index = index_full
        if(index!=-1):
            str = trim[0:index]
        else:
            str = trim
        resultset.append(str)
        return resultset


def search_function():
    result = []
    final_result = []
    file_txt = open("SearchFile.txt","r")
    for line in file_txt:
        line = line.strip()
        words = line.split(' ')
        for f in words:
            if(f.__contains__('RL50')):
                result.append(f)

    x = np.array(result)
    unique_list = np.unique(x)
    trimmed_list = []
    for trim in unique_list:
        index_under = trim.rfind('_')
        index_full = trim.find('.') 
        if index_under != None and index_under != 4:
            index=index_under
        else:
            index = index_full
        if(index!=-1):
            str = trim[0:index]
        else:
            str = trim
        trimmed_list.append(str)
        adhoc_trim = []
        for trim in trimmed_list:
            index_under = trim.rfind('_')
        index_full = trim.find('.') 
        if index_under != None and index_under != 4:
            index=index_under
        else:
            index = index_full
        if(index!=-1):
            str = trim[0:index]
        else:
            str = trim
        adhoc_trim.append(str)
        y = np.array(adhoc_trim)
        unique_list1 = np.unique(y)
        final_result.append(str)
        file_txt.close()
    un = np.array(final_result)
    un_res = np.unique(un)
    un_res_final = np.unique(un_res)
    final_print = ''
    for item in un_res:
        if (item[-1]) != '0':
            final_print = final_print + item + '\n'
    #print(final_print)
    result_file = open('ResultFile.txt', 'w+')
    result_file.write(final_print)
    result_file.close()    

def loadcall():
# A List of Items
    items = list(range(0, 57))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.0000000000000000000000000000000001)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


if __name__ == '__main__':
    root_path = os.getcwd()
    process_flag = True
    try:
        file_txt = open("SearchFile.txt","r")
    except IOError:
        print('\n ======= Validations invoked ===========')
        print('\n Error : File SearchFile.txt not found within ' + root_path + '\ directory. Kindly ensure the file present with contents to search.\n')
        print(' ======= Please resolve these in order to proceed ======')
        process_flag = False
    if process_flag == True and os.path.getsize(root_path+'\SearchFile.txt') == 0:
        print('\n ======= Validations invoked ===========')
        print('\n Error : File SearchFile.txt is empty within directory '+ root_path + '. Kindly ensure the file has some contents to search.\n')
        print(' ======= Please resolve these in order to proceed ======\n\n')
        process_flag = False

    if process_flag == True:
        print('\n============= Threads Initializing : =========  \n')
        t = threading.Thread(target=search_function).start()
        q = threading.Thread(target=loadcall()).start()

        print('\nFile path : -- ' +  '\ResultFile.txt\n')
        print('\n===================== Completed : ==================  \n')
    file_txt.close
    pause()