#!/usr/bin/python

#  Author: Kurt Jacobson
#  Date: 04/15/17
#  Email: kurtcjacobson@gmail.com
#  License: GPL

# DESCRIPTION
#  Userspace HAL component for LinuxCNC that creates two HAL pins 
#  indicating the current G20/G21 state

import hal, time
import linuxcnc

stat = linuxcnc.stat()

h = hal.component("units")
h.newpin("prog_in", hal.HAL_BIT, hal.HAL_OUT)
h.newpin("prog_mm", hal.HAL_BIT, hal.HAL_OUT)
h.newpin("update_rate", hal.HAL_FLOAT, hal.HAL_IN)

h.ready()

# Set default update rate to 100ms
h.update_rate = .1

try:
    while 1:
        time.sleep(h.update_rate)
        stat.poll()
        prog_units = stat.program_units
        if prog_units == 1: # Inch
            h.prog_in = 1
            h.prog_mm = 0
        elif prog_units == 2: # Metric
            h.prog_in = 0
            h.prog_mm = 1
except KeyboardInterrupt:
    raise SystemExit
