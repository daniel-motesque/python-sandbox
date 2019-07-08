"""
import os

os.environ['LD_LIBRARY_PATH'] = "/usr/local/lib"
"""

import pychrono as chrono

my_vect1   = chrono.ChVectorD()

my_vect1.x=5
my_vect1.y=2
my_vect1.z=3

my_vect2 = chrono.ChVectorD(3,4,5)
my_vect4 = my_vect1*10 + my_vect2

my_len = my_vect4.Length()
print ('vector length =', my_len)


