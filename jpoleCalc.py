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

da = datetime.datetime.now()
example = 446.1

def linea():
    print("----------------------------------------")

def usage():
    print(f"{argv[0]} {__version__}")
    print(f"{__copyright__} {__author__}\n")
    print("Usage:")
    print(f"$> python {argv[0]} {example}\n")

if len(argv) < 2:
    usage()
    print(f"Need Frequency !!! \n")
    exit(1)

try:
    x = float(argv[1])
except ValueError:
    usage()
    print("Use float number!\n")
    exit()

f = float(argv[1]) * 1e6          # Frequency
c = 299_792_458                   # Speed of light ~
vf = 0.96                         # Velocity factor Cooper and Alu

##################################################################
########## Calculations ##########
'''
Long section dimension (A)      0.75 * l * vf
Short section dimension (B)     (l/4) * vf
Feed point dimension (C)        (l/50) * vf  - the correct formula is (l/40) * vf  
Spacing dimension (D)           (0.045 * l) / 2
'''
l = c / f

a = l * 0.75 * vf * 1e3
b = (l / 4) * vf * 1e3
c = (l / 40) * vf * 1e3
d = (0.045 * l) / 2 * 1e3

linea()
print("       - J-Pole Antenna Design -")
linea()
print(f" The frequency is  : ", end='')
cprint(f"{argv[1]} MHz", "yellow")
print(f" The lambda is     : {l*1e3:.1f} mm")
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
