from functions.util.helper_functions import *
from functions.util.unit_conversions import *
from functions.util.regions import *

def sV_p(pressure):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            return s2_pT(pressure, T4_p(pressure))
        else:
            return s3_rhoT(1 / (v3_ph(pressure, h4V_p(pressure))), T4_p(pressure))
    else:
        return "Error"

def sL_p(pressure):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            return s1_pT(pressure, T4_p(pressure))
        else:
            return s3_rhoT(1 / (v3_ph(pressure, h4L_p(pressure))), T4_p(pressure))
    else:
        return "Error"

def sV_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature < 647.096:
        if temperature <= 623.15:
            return s2_pT(p4_T(temperature), temperature)
        else:
            return s3_rhoT(1 / (v3_ph(p4_T(temperature), h4V_p(p4_T(temperature)))), temperature)
    else:
        return "Error"

def sL_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature < 647.096:
        if temperature <= 623.15:
            return s1_pT(p4_T(temperature), temperature)
        else:
            return s3_rhoT(1 / (v3_ph(p4_T(temperature), h4L_p(p4_T(temperature)))), temperature)
    else:
        return "Error"

def s_pT(pressure, temperature):
    pressure = toSI_p(pressure)
    temperature = toSI_T(temperature)
    region = region_pT(pressure, temperature)

    if region == 1:
        return s1_pT(pressure, temperature)
    elif region == 2:
        return s2_pT(pressure, temperature)
    elif region == 3:
        return s3_rhoT(1 / v3_ph(pressure, h3_pT(pressure, temperature)), temperature)
    elif region == 4:
        return "Error"
    elif region == 5:
        return s5_pT(pressure, temperature)
    else:
        return "Error"

def s_ph(pressure, enthalpy):
    pressure = toSI_p(pressure)
    region = region_ph(pressure, enthalpy)

    if region == 1:
        return s1_pT(pressure, T1_ph(pressure, enthalpy))
    elif region == 2:
        return s2_pT(pressure, T2_ph(pressure, enthalpy))
    elif region == 3:
        return s3_rhoT(1 / v3_ph(pressure, enthalpy), T3_ph(pressure, enthalpy))
    elif region == 4:
        Ts = T4_p(pressure)
        xs = x4_ph(pressure, enthalpy)
        if pressure < 16.529:
            s4V = s2_pT(pressure, Ts)
            s4L = s1_pT(pressure, Ts)
        else:
            v4V = v3_ph(pressure, h4V_p(pressure))
            s4V = s3_rhoT(1 / v4V, Ts)
            v4L = v3_ph(pressure, h4L_p(pressure))
            s4L = s3_rhoT(1 / v4L, Ts)

        return xs * s4V + (1 - xs) * s4L
    elif region == 5:
        return s5_pT(pressure, T5_ph(pressure, enthalpy))
    else:
        return "Error"