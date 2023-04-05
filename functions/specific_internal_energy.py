from functions.util.unit_conversions import *
from functions.util.helper_functions import *
from functions.util.regions import *

def uV_p(pressure):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            return u2_pT(pressure, T4_p(pressure))
        else:
            return u3_rhoT(1 / (v3_ph(pressure, h4V_p(pressure))), T4_p(pressure))
    else:
        return "Error"

def uL_p(pressure):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            return u1_pT(pressure, T4_p(pressure))
        else:
            return u3_rhoT(1 / (v3_ph(pressure, h4L_p(pressure))), T4_p(pressure))
    else:
        return "Error"

def uV_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature < 647.096:
        if temperature <= 623.15:
            return u2_pT(p4_T(temperature), temperature)
        else:
            return u3_rhoT(1 / (v3_ph(p4_T(temperature), h4V_p(p4_T(temperature)))), temperature)
    else:
        return "Error"

def uL_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature < 647.096:
        if temperature <= 623.15:
            return u1_pT(p4_T(temperature), temperature)
        else:
            return u3_rhoT(1 / (v3_ph(p4_T(temperature), h4L_p(p4_T(temperature)))), temperature)
    else:
        return "Error"

def u_pT(pressure, temperature):
    pressure = toSI_p(pressure)
    temperature = toSI_T(temperature)
    region = region_pT(pressure, temperature)

    if region == 1:
        return u1_pT(pressure, temperature)
    elif region == 2:
        return u2_pT(pressure, temperature)
    elif region == 3:
        return u3_rhoT(1 / v3_ph(pressure, h3_pT(pressure, temperature)), temperature)
    elif region == 4:
        return "Error"
    elif region == 5:
        return u5_pT(pressure, temperature)
    else:
        return "Error"

def u_ph(pressure, enthalpy):
    pressure = toSI_p(pressure)
    region = region_ph(pressure, enthalpy)

    if region == 1:
        return u1_pT(pressure, T1_ph(pressure, enthalpy))
    elif region == 2:
        return u2_pT(pressure, T2_ph(pressure, enthalpy))
    elif region == 3:
        return u3_rhoT(1 / v3_ph(pressure, enthalpy), T3_ph(pressure, enthalpy))
    elif region == 4:
        Ts = T4_p(pressure)
        xs = x4_ph(pressure, enthalpy)
        if pressure < 16.529:
            u4v = u2_pT(pressure, Ts)
            u4L = u1_pT(pressure, Ts)
        else:
            v4V = v3_ph(pressure, h4V_p(pressure))
            u4v = u3_rhoT(1 / v4V, Ts)
            v4L = v3_ph(pressure, h4L_p(pressure))
            u4L = u3_rhoT(1 / v4L, Ts)

        return xs * u4v + (1 - xs) * u4L
    elif region == 5:
        Ts = T5_ph(pressure, enthalpy)
        return u5_pT(pressure, Ts)
    else:
        return "Error"

def u_ps(pressure, entropy):
    pressure = toSI_p(pressure)
    region = region_ps(pressure, entropy)

    if region == 1:
        return u1_pT(pressure, T1_ps(pressure, entropy))
    elif region == 2:
        return u2_pT(pressure, T2_ps(pressure, entropy))
    elif region == 3:
        return u3_rhoT(1 / v3_ps(pressure, entropy), T3_ps(pressure, entropy))
    elif region == 4:
        if pressure < 16.529:
            uLp = u1_pT(pressure, T4_p(pressure))
            uVp = u2_pT(pressure, T4_p(pressure))
        else:
            uLp = u3_rhoT(1 / (v3_ph(pressure, h4L_p(pressure))), T4_p(pressure))
            uVp = u3_rhoT(1 / (v3_ph(pressure, h4V_p(pressure))), T4_p(pressure))
        
        x = x4_ps(pressure, entropy)
        return x * uVp + (1 - x) * uLp
    else:
        return "Error"