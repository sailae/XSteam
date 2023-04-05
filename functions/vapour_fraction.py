from functions.util.helper_functions import *
from functions.util.unit_conversions import *

def x_ph(pressure, enthalpy):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        return x4_ph(pressure, enthalpy)
    else:
        return "Error"

def x_ps(pressure, entropy):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        return x4_ps(pressure, entropy)
    else:
        return "Error"