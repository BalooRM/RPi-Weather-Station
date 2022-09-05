#!/usr/bin/python3
# convert text log to CSV
# 05-Sep-2022
#
import datetime
import time
import sys

def read_in():
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
    return lines

def eprint(*args, **kwargs):
    # print errors and other non-data messages to stderr
    print(*args, file=sys.stderr, **kwargs)

starttime = datetime.datetime.now()
eprint(starttime)

lines = read_in()

endtime = datetime.datetime.now()
eprint(endtime)

eprint(str(len(lines)) + ' lines read...')

print(','.join(['Timestamp', 'Date', 'Hour', 'DegC', 'DegF', 'RelHumPct']))
myx = []
myy1 = []
myy2 = []
myy3 = []
for i in range(len(lines)):
    mykey = lines[i][:10]
    mytime = lines[i][11:16]
    mystart = lines[i].find("(") + 1
    myend = lines[i].find(" F)")
    mystart1 = lines[i].find("Temp: ") + 6
    myend1 = lines[i].find("C")
    mystart2 = lines[i].find("ity:") + 4
    myend2 = lines[i].find(" \%")
    myval = float(lines[i][mystart:myend]) # extract temp F and convert to float
    myval1 = float(lines[i][mystart1:myend1]) # extract temp C and convert to float    
    myval2 = float(lines[i][mystart2:myend2]) # extract humidity and convert to float
    mytimepoint = lines[i][:23]
    try:
        mytuple = time.strptime(mytimepoint, "%Y-%m-%d %H:%M:%S %Z")
        mydt = datetime.datetime(mytuple[0], mytuple[1], mytuple[2], mytuple[3], mytuple[4])
        myx.append(mydt.strftime("%Y-%m-%d %H:%M"))
        #print(list(mytuple))
        print(','.join([mytimepoint, mykey, str(mytuple[3]), str(myval1), str(myval), str(myval2)]))
        myy1.append(myval)
        myy2.append(myval1)
        myy3.append(myval2)
    except Exception as e:
        eprint(e)
        eprint('line ' + str(i))
        eprint(lines[i])
        # pass
