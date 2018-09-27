#!/usr/bin/python

import sys
import time
import Adafruit_DHT

#while True:

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18)
fahrenheit = temperature * 9. / 5. + 32
myTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
# disregard the first reading
#print '{3} Temp: {0:0.1f} C ({1:0.1f} F) Humidity: {2:0.1f} %'.format(temperature, fahrenheit, humidity, myTimeStamp)

time.sleep(1.5);
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18)
hsum = humidity
tsum = temperature
#fahrenheit = temperature * 9. / 5. + 32
#myTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
#print '{3} Temp: {0:0.1f} C ({1:0.1f} F) Humidity: {2:0.1f} %'.format(temperature, fahrenheit, humidity, myTimeStamp)

time.sleep(1.5);
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18)
hsum += humidity
tsum += temperature
#fahrenheit = temperature * 9. / 5. + 32
#myTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
#print '{3} Temp: {0:0.1f} C ({1:0.1f} F) Humidity: {2:0.1f} %'.format(temperature, fahrenheit, humidity, myTimeStamp)

time.sleep(1.5);
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18)
hsum += humidity
tsum += temperature
#fahrenheit = temperature * 9. / 5. + 32
#myTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
#print '{3} Temp: {0:0.1f} C ({1:0.1f} F) Humidity: {2:0.1f} %'.format(temperature, fahrenheit, humidity, myTimeStamp)
time.sleep(1.5);

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18)
hsum += humidity
tsum += temperature
#fahrenheit = temperature * 9. / 5. + 32
#myTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
#print '{3} Temp: {0:0.1f} C ({1:0.1f} F) Humidity: {2:0.1f} %'.format(temperature, fahrenheit, humidity, myTimeStamp)

time.sleep(1.5);
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18)
hsum += humidity
tsum += temperature
#fahrenheit = temperature * 9. / 5. + 32
#myTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")
#print '{3} Temp: {0:0.1f} C ({1:0.1f} F) Humidity: {2:0.1f} %'.format(temperature, fahrenheit, humidity, myTimeStamp)

humidity = hsum / 5.
temperature = tsum / 5.
fahrenheit = temperature * 9. / 5. + 32
myTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S %Z")

print '{3} Temp: {0:0.1f} C ({1:0.1f} F) Humidity: {2:0.1f} %'.format(temperature, fahrenheit, humidity, myTimeStamp)


