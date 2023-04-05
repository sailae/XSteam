from functions.util.unit_conversions import *
from functions.util.regions import *
from functions.util.transport_properties import *
from functions.enthalpy import *

def my_pT(pressure, temperature):
    pressure = toSI_p(pressure)
    temperature = toSI_T(temperature)
    region = region_pT(pressure, temperature)

    if region == 4:
        return "Error"
    elif region == 1 or region == 2 or region == 3 or region == 5:
        return my_AllRegions_pT(pressure, temperature)
    else:
        return "Error"

def my_ph(pressure, enthalpy):
    pressure = toSI_p(pressure)
    region = region(pressure, enthalpy)

    if region == 4:
        return "Error"
    elif region == 1 or region == 2 or region == 3 or region == 5:
        return my_AllRegions_ph(pressure, enthalpy)
    else:
        return "Error"

def my_ps(pressure, entropy):
    return my_ph(pressure, h_ps(pressure, entropy))