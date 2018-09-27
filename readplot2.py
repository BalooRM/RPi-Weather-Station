#!/usr/bin/python
# uses pyGnuplot
'''
$Header: /var/lib/cvsroot/weather/readplot2.py,v 1.4 2017/11/13 01:13:13 pi Exp $
'''
import sys
import time
from datetime import datetime, timedelta
import pyGnuplot

mydebug = 0
dmintF = dict()
dmaxtF = dict()
dmintFtime = dict() # time of minimum temperature
dmaxtFtime = dict() # time of maximum temperature
mytoday = time.strftime("%Y-%m-%d")
mynow = time.strftime("%H:%M")
# determine graph start time from time now
deltahours = 24
mytt = time.strptime(time.strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # tuple time
mydt = datetime(mytt[0], mytt[1], mytt[2], mytt[3], mytt[4])
mydtstart = mydt
mydtstart += timedelta(hours=-deltahours)
#print "mydtstart", mydtstart
# Create arrays for x and y data. These will need to be tuples for plotting.
myx = []
myy1 = []
myy2 = []

def qw(s1):
    return "{}".format(s1)

def read_in():
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
    return lines

def main():
    lines = read_in()
    for i in range(len(lines)):
        mykey = lines[i][:10]
        mytime = lines[i][11:16]
        mystart = lines[i].find("(") + 1
        myend = lines[i].find(" F)")
        mystart2 = lines[i].find("ity:") + 4
        myend2 = lines[i].find(" \%")
        myval = float(lines[i][mystart:myend]) # extract temp F and convert to float
        myval2 = float(lines[i][mystart2:myend2]) # extract humidity and convert to float
        mytimepoint = lines[i][:23]
        mytuple = time.strptime(mytimepoint, "%Y-%m-%d %H:%M:%S %Z")
        mydt = datetime(mytuple[0], mytuple[1], mytuple[2], mytuple[3], mytuple[4])
        if mydt > mydtstart:
            myx.append(mydt.strftime("%Y-%m-%d %H:%M"))
            myy1.append(myval)
            myy2.append(myval2)
            
        # get daily min and max temp F
        if mykey in dmintF: # if key exists for min, it exists for max
            if myval < dmintF[mykey]:
                dmintF[mykey] = myval
                dmintFtime[mykey] = mytime
            if myval > dmaxtF[mykey]:
                dmaxtF[mykey] = myval
                dmaxtFtime[mykey] = mytime
            #print 'min =', dmintF[mykey]
            #print 'max =', dmaxtF[mykey]
        else: # if key does not exist, set min and max = myval
            dmintF[mykey] = myval
            dmintFtime[mykey] = mytime
            dmaxtF[mykey] = myval
            dmaxtFtime[mykey] = mytime
        # end of daily min and max temp F
    # end for
    
    mytx = tuple(myx)
    #mytx = [datetime.strptime(i, '%Y-%m-%d %H:%M') for i in myx]
    myty1 = tuple(myy1)
    myty2 = tuple(myy2)

    print 'Daily temperature ranges (F):'
    for mykey in sorted(dmintF):
        print mykey, ': min =', dmintF[mykey], '(@', dmintFtime[mykey], ') max =', dmaxtF[mykey], '(@', dmaxtFtime[mykey], ')'
        #print dmintF
        #print dmaxtF
    # output graph to png file
    g1 = pyGnuplot.gnuplot() #debug=1)
    g1('set xdata time')
    g1('set timefmt "%Y-%m-%d %H:%M"')
    g1('set format x "%m/%d\\n%Hh"')
    g1('set title "Temperature (F) and Rel. Humidity for the Last 24 Hours"')
    g1('set xtics font ", 10"')
    g1('set xlabel "Time (MM/DD HHh)"')
    g1('set ylabel "Temperature (F)\\nRel. Humidity (\%)"')
    g1('set y2tics')
    # plot temperature
    plt=g1.plot(myty1, xvals=mytx, title="Temp", style="lines", u="1:3")
    # add humidity
    plt.add(myty2, xvals=mytx, title="Rel. Humidity", style="lines", u="1:3")
    g1('set grid')
    g1.hardcopy(plt, file='/scratch/weather/24hours.png', size='780,464',truecolor=True)
    del g1


main()


