from functions.util.helper_functions import *
from functions.util.unit_conversions import *
from functions.util.regions import *

def CpV_p(pressure):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            return Cp2_pT(pressure, T4_p(pressure))
        else:
            return Cp3_rhoT(1 / (v3_ph(pressure, h4V_p(pressure))), T4_p(pressure))
    else:
        return "Error"

def CpL_p(pressure):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            return Cp1_pT(pressure, T4_p(pressure))
        else:
            T = T4_p(pressure)
            h = h4L_p(pressure)
            v = v3_ph(pressure, h4L_p(pressure))
            return Cp3_rhoT(1 / (v3_ph(pressure, h4L_p(pressure))), T4_p(pressure))
    else:
        return "Error"

def CpV_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature < 647.096:
        if temperature <= 623.15:
            return Cp2_pT(p4_T(temperature), temperature)
        else:
            return Cp3_rhoT(1 / (v3_ph(p4_T(temperature), h4V_p(p4_T(temperature)))), temperature)
    else:
        return "Error"

def CpL_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature < 647.096:
        if temperature <= 623.15:
            return Cp1_pT(p4_T(temperature), temperature)
        else:
            return Cp3_rhoT(1 / (v3_ph(p4_T(temperature), h4L_p(p4_T(temperature)))), temperature)
    else:
        return "Error"

def Cp_pT(pressure, temperature):
    pressure = toSI_p(pressure)
    temperature = toSI_T(temperature)
    region = region_pT(pressure, temperature)

    if region == 1:
        return Cp1_pT(pressure, temperature)
    elif region == 2:
        return Cp2_pT(pressure, temperature)
    elif region == 3:
        return Cp3_rhoT(1 / v3_ph(pressure, h3_pT(pressure, temperature)), temperature)
    elif region == 4:
        return "Error"
    elif region == 5:
        return Cp5_pT(pressure, temperature)
    else:
        return "Error"

def Cp_ph(pressure, enthalpy):
    pressure = toSI_p(pressure)
    region = region_ph(pressure, enthalpy)

    if region == 1:
        return Cp1_pT(pressure, T1_ph(pressure, enthalpy))
    elif region == 2:
        return Cp2_pT(pressure, T2_ph(pressure, enthalpy))
    elif region == 3:
        return Cp3_rhoT(1 / v3_ph(pressure, enthalpy), T3_ph(pressure, enthalpy))
    elif region == 4:
        return "Error"
    elif region == 5:
        return Cp5_pT(pressure, T5_ph(pressure, enthalpy))
    else:
        return "Error"

def Cp_ps(pressure, entropy):
    pressure = toSI_p(pressure)
    entropy = entropy
    region = region_ps(pressure, entropy)

    if region == 1:
        return Cp1_pT(pressure, T1_ps(pressure, entropy))
    elif region == 2:
        return Cp2_pT(pressure, T2_ps(pressure, entropy))
    elif region == 3:
        return Cp3_rhoT(1 / v3_ps(pressure, entropy), T3_ps(pressure, entropy))
    elif region == 4:
        return "Error"
    elif region == 5:
        return Cp5_pT(pressure, T5_ps(pressure, entropy))
    else:
        return "Error"