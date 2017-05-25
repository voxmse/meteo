from Adafruit_BME280 import *
import sys
import time
import os.path

currenttime = time.strftime('%Y%m%d%H%M')
datafilepath = sys.argv[1] + "/" + currenttime[0:8] + ".csv"

lasttime = "000000000000"
if os.path.isfile(datafilepath):
  with open(datafilepath) as datafile:
    for dataline in datafile.readlines():
     lasttime = dataline.split(",")[0]

print lasttime

if currenttime>lasttime:
  sensor = BME280(mode=BME280_OSAMPLE_8)
  degrees = sensor.read_temperature()
  pascals = sensor.read_pressure()
  mmhg = pascals /1000 * 760 / 101.325
  humidity = sensor.read_humidity()
  with open(datafilepath, "a") as datafile:
    datafile.write(currenttime+","+'{0:0.3f}'.format(degrees)+","+'{0:0.3f}'.format(mmhg)+","+'{0:0.2f}'.format(humidity)+"\n")
