from functions.util.helper_functions import *
from functions.util.unit_conversions import *
from functions.util.regions import *

def vV_p(pressure):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            return v2_pT(pressure, T4_p(pressure))
        else:
            v3_ph(pressure, h4V_p(pressure))
    else:
        return "Error"

def vL_p(pressure):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            return v1_pT(pressure, T4_p(pressure))
        else:
            return v3_ph(pressure, h4L_p(pressure))
    else:
        return "Error"

def vV_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature < 647.096:
        if temperature <= 623.15:
            return v2_pT(p4_T(temperature), temperature)
        else:
            return v3_ph(p4_T(temperature), h4V_p(p4_T(temperature)))
    else:
        return "Error"

def vL_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature < 647.096:
        if temperature <= 623.15:
            return v1_pT(p4_T(temperature), temperature)
        else:
            return v3_ph(p4_T(temperature), h4L_p(p4_T(temperature)))
    else:
        return "Error"

def v_pT(pressure, temperature):
    pressure = toSI_p(pressure)
    temperature = toSI_T(temperature)
    region = region_pT(pressure, temperature)

    if region == 1:
        return v1_pT(pressure, temperature)
    elif region == 2:
        return v2_pT(pressure, temperature)
    elif region == 3:
        return v3_ph(pressure, h3_pT(pressure, temperature))
    elif region == 4:
        return "Error"
    elif region == 5:
        return v5_pT(pressure, temperature)
    else:
        return "Error"

def v_ph(pressure, enthalpy):
    pressure = toSI_p(pressure)
    region = region_ph(pressure, enthalpy)

    if region == 1:
        return v1_pT(pressure, T1_ph(pressure, enthalpy))
    elif region == 2:
        return v2_pT(pressure, T2_ph(pressure, enthalpy))
    elif region == 3:
        return v3_ph(pressure, enthalpy)
    elif region == 4:
        xs = x4_ph(pressure, enthalpy)
        if pressure < 16.529:
            v4V = v2_pT(pressure, T4_p(pressure))
            v4L = v1_pT(pressure, T4_p(pressure))
        else:
            v4V = v3_ph(pressure, h4V_p(pressure))
            v4L = v3_ph(pressure, h4L_p(pressure))
        return xs * v4V + (1 - xs) * v4L
    elif region == 5:
        return v5_pT(pressure, T5_ph(pressure, enthalpy))
    else:
        return "Error"

def v_ps(pressure, entropy):
    pressure = toSI_p(pressure)
    region = region_ps(pressure, entropy)

    if region == 1:
        return v1_pT(pressure, T1_ps(pressure, entropy))
    elif region == 2:
        return v2_pT(pressure, T2_ps(pressure, entropy))
    elif region == 3:
        return v3_ps(pressure, entropy)
    elif region == 4:
        xs = x4_ps(pressure, entropy)
        if pressure < 16.529:
            v4V = v2_pT(pressure, T4_p(pressure))
            v4L = v1_pT(pressure, T4_p(pressure))
        else:
            v4V = v3_ph(pressure, h4V_p(pressure))
            v4L = v3_ph(pressure, h4L_p(pressure))

        return xs * v4V + (1 - xs) * v4L
    elif region == 5:
        return v5_pT(pressure, T5_ps(pressure, entropy))
    else:
        return "Error"