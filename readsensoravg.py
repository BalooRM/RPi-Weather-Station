#!/usr/bin/python
# R. Ballew 05-Sep-2022
# Read, average and output sensor values
# This replaces dht22webavg.py and can be scheduled with crontab.
import Adafruit_DHT
import time
import sys

def eprint(*args, **kwargs):
    # print errors and other non-data messages to stderr
    print(*args, file=sys.stderr, **kwargs)

def strnumdp(n, dp):
    # format numbers as str with decimal places
    val = int(n * pow(10, dp)) / pow(10, dp)
    return str(val)

    
sensor = Adafruit_DHT.DHT22  # DHT11 # DHT22
gpio_pin = 18    # Raspberry Pi GPIO pin number
avgs = 5         # number of readings to make
rcounts = 0      # actual number of in-range readings
minDegC = -40.0  # sensor minimum temperature
maxDegC = 80.0   # sensor maximum temperature
minHum = 0.0     # sensor minimum humidity
maxHum = 100.0   # sensor maximum humidity
hsum = 0
Csum = 0
Fsum = 0

debug = False
# disregard the first reading
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)

# read temp and humidity and print to append to file as CSV
#### Timestamp,Date,Hour,DegC,DegF,RelHumPct
#### 2022-09-04 21:00:18 EDT,2022-09-04,21,25.1,77.1,99.9

myTimestamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
if debug:
    print(','.join(['Timestamp','Date','Hour','DegC','DegF','RelHumPct']))
for i in range(0, avgs):
    time.sleep(1.5);
    myTimestamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)
    fahrenheit = temperature * 9. / 5. + 32
     
    if debug:
        # print('{3} Temp: {0:0.1f} C ({1:0.1f} F) Humidity: {2:0.1f} %'.format(temperature, fahrenheit, humidity, myTimestamp))
        print(','.join([myTimestamp, time.strftime('%Y-%m-%d'), time.strftime('%H'), strnumdp(temperature, 1), strnumdp(fahrenheit, 1), strnumdp(humidity, 1) ]))
    if ((minDegC <= temperature) and (temperature <= maxDegC) and (minHum <= humidity) and (humidity <= maxHum)):
        rcounts += 1
        hsum += humidity
        Csum += temperature
        Fsum += fahrenheit
    else:
        eprint('Alert: Temperature or humidity out of range.')
        eprint(','.join([myTimestamp, time.strftime('%Y-%m-%d'), time.strftime('%H'), strnumdp(temperature, 1), strnumdp(fahrenheit, 1), strnumdp(humidity, 1) ]))

# print('{3} Temp: {0:0.1f} C ({1:0.1f} F) Humidity: {2:0.1f} %'.format(temperature, fahrenheit, humidity, myTimestamp))
myTimestamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
if rcounts > 0:
    humidity = hsum / rcounts
    temperature = Csum / rcounts
    fahrenheit = Fsum / rcounts
    print(','.join([myTimestamp, time.strftime('%Y-%m-%d'), time.strftime('%H'), strnumdp(temperature, 1), strnumdp(fahrenheit, 1), strnumdp(humidity, 1) ]))
else:
    eprint('Warning: ' + myTimestamp + ' - Error reading sensor.')

