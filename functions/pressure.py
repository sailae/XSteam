from functions.util.unit_conversions import *
from functions.util.helper_functions import *
from functions.util.regions import *
from functions.specific_volume import *

def psat_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature <= 647.096:
        return fromSI_p(p4_T(temperature))
    else:
        return "Error"

def psat_s(entropy):
    if -0.0001545495919 < entropy < 9.155759395:
        return fromSI_p(p4_s(entropy))
    else:
        return "Error"

def p_hs(enthalpy, entropy):
    if region_hs(enthalpy, entropy) == 1:
        return fromSI_p(p1_hs(enthalpy, entropy))
    elif region_hs(enthalpy, entropy) == 2:
        return fromSI_p(p2_hs(enthalpy, entropy))
    elif region_hs(enthalpy, entropy) == 3:
        return fromSI_p(p3_hs(enthalpy, entropy))
    elif region_hs(enthalpy, entropy) == 4:
        return fromSI_p(p4_T(T4_hs(enthalpy, entropy)))
    elif region_hs(enthalpy, entropy) == 5:
        return "Error"
    else:
        return "Error"

def p_hrho(enthalpy, density):
    high_bound = fromSI_p(100)
    low_bound = fromSI_p(0.000611657)
    pressure = fromSI_p(10)
    densities = 1 / v_ph(pressure, enthalpy)
    while abs(density - densities) > 10^(-7):
        densities = 1 / v_ph(pressure, enthalpy)
        if densities >= density:
            high_bound = pressure
        else:
            low_bound = pressure
        pressure = (low_bound + high_bound) / 2

    return pressure

