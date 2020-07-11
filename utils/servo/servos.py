import time

import pigpio  # http://abyz.me.uk/rpi/pigpio/python.html

SERVOS=[14, 15, 16, 17, 18, 19] # List of GPIO connected to servos.

MIN_SERVO=500
MAX_SERVO=2500

MIN_POT_CAP=0
MAX_POT_CAP=1023

def map(val, in_min, in_max, out_min, out_max):
  return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

pi = pigpio.pi() # Connect to Pi.

if not pi.connected:
  exit()

adc = pi.spi_open(0, 40000) # Open SPI channel 0 at 40kbps.

while True:

   try:

     for i in range(len(SERVOS)):

        # This code assumes that an 8-channel MCP3008 ADC is connected
        # to the main SPI channel 0

        c, d = pi.spi_xfer(adc, [1, (8+i)<<4, 0]) # Read channel i.

        v = ((d[1]<<8) | d[2]) & 0x3FF

        micros = map(v, MIN_POT_CAP, MAX_POT_CAP, MIN_SERVO, MAX_SERVO)

        pi.set_servo_pulsewidth(SERVOS[i], micros)

     time.sleep(0.02)

   except:

      break

print("\nexiting...")

pi.spi_close(adc) # Release SPI handle.

for s in SERVOS:
   pi.set_servo_pulsewidth(s, 0) # Switch each servo off.

pi.stop() # Disconnect from Pi.
Here is some code I have used to control a servo with a pot connected to a capacitor charge/discharge circuit. The time taken to charge the capacitor is used to get a pot measurement to feed into the servo setting.

Short video showing the operation.

#!/usr/bin/env python

# servo_pot_cap.py
# 2016-01-16
# Public Domain

import time

import pigpio  # abyz.me.uk/rpi/pigpio/python.html
import pot_cap # abyz.me.uk/rpi/pigpio/examples.html#Python_pot_cap_py

SERVO=21
POT_CAP=4

MIN_SERVO=1000
MAX_SERVO=2000

MIN_POT_CAP=10
MAX_POT_CAP=470

def map(val, in_min, in_max, out_min, out_max):
   return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

pi = pigpio.pi() # Connect to Pi.

if not pi.connected:
   exit(0)

pc = pot_cap.reader(pi, POT_CAP, 1, 1)

try:

   while True:

      s, v, r = pc.read()

      if s: # Valid reading.

         if v < MIN_POT_CAP:
            v = MIN_POT_CAP

         if v > MAX_POT_CAP:
            v = MAX_POT_CAP

         micros = map(v, MIN_POT_CAP, MAX_POT_CAP, MIN_SERVO, MAX_SERVO)

         pi.set_servo_pulsewidth(SERVO, micros)

         time.sleep(0.02)

except:
   pass

print("\nexiting...")

pc.cancel() # Cancel pot cap reader.
pi.stop() # Disconnect from Pi.