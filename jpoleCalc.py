#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Zsolt Peto"
__license__ = "MIT"
__copyright__ = "Copyright 2026"
__version__ = "0.1"
__status__ = "Stable"

from sys import argv, exit
from termcolor import cprint
import datetime
from math import log10

da = datetime.datetime.now()
example = 145.9
tube_example = 15

def linea():
    print("----------------------------------------")

def usage():
    print(f"{argv[0]} {__version__}")
    print(f"{__copyright__} {__author__}\n")
    print("Usage:")
    print(f"$> python {argv[0]} {example} {tube_example}\n")

if len(argv) < 3:
    usage()
    print(f"Need Frequency and tube diameter !!!\n")
    exit(1)

try:
    x = float(argv[1])
    y = float(argv[2]) 
    if x <= 0:
        raise ValueError
    if y <= 0:
        raise ValueError
except ValueError:
    usage()
    print("Use float number !")
    print("The number is zero or smaller then zero\n")
    exit()

f_mhz = float(argv[1])              # Frequency
c = 299792.458                      # Speed of light ~
d_tube = float(argv[2])             # Tube diameter



##################################################################
########## Calculations ##########
'''
Long section dimension (A)      0.75 * l * vf
Short section dimension (B)     (l/4) * vf
Feed point dimension (C)        (l/50) * vf  - the correct formula is (l/40) * vf  
Spacing dimension (D)           (0.045 * l) / 2
'''
l_mm = (c / f_mhz)
l = (c*1e3) / (f_mhz*1e6)
#print(l)
# 1. Slenderness factor (L/d ratio)
# The thicker the pipe, the lower the velocity factor (K-factor)
ratio = (l_mm / 2) / d_tube
# Empirical formula for thick bars:
vf = 0.99 - (0.5 / (log10(ratio) * 10))
#vf = 0.96
# 2. End Effect Correction
# Due to the thickness of the tube, the field "exits" at the end, which corresponds to approximately 0.3-0.5 * diameter
# extra length electrically. This must be subtracted from the physical length!

# end_correction = 0.43 * d_tube

'''
a = (l_mm * 0.75 * vf) # - end_correction
b = ((l_mm / 4) * vf ) # - end_correction
c = ((l_mm / 40) * vf )
d = (0.045 * l_mm) / 2 # 0.45 origin 
'''
a = l * 0.75 * vf * 1e3
b = (l / 4) * vf * 1e3
c = (l / 40) *vf * 1e3
d = ((0.045 * l) / 2) * 1e3

linea()
print("       - J-Pole Antenna Design -")
linea()
print(f" The frequency is  : ", end='')
cprint(f"{argv[1]} MHz", "yellow")
print(f" The lambda is     : {l_mm:.1f} mm")
print(f" The tube diameter : ", end='')
cprint(f"{d_tube:.1f} mm", "blue")
linea()
print(f" Long section element   : ", end='')
cprint(f"{a:.1f} mm", "green")
print(f" Short section element  : ", end='')
cprint(f"{b:.1f} mm", "green")
print(f" Feed point             : ", end='')
cprint(f"{c:.1f} mm", "blue")
print(f" Spacing                : ", end='')
cprint(f"{d:.1f} mm", "yellow")

linea()
print("        ", end='')
cprint(da.strftime("%c"), "green")
linea()
########## END ##########
