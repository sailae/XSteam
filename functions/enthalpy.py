from functions.util.helper_functions import *
from functions.util.unit_conversions import *
from functions.util.regions import *

def hV_p(pressure):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        return h4V_p(pressure)
    else:
        return "Error"

def hL_p(pressure):
    pressure = toSI_p(pressure)

    if 0.000611657 < pressure < 22.06395:
        return h4L_p(pressure)
    else:
        return "Error"

def hV_T(temperature):
    temperature = toSI_T(temperature)
    if 273.15 < temperature < 647.096:
        return h4V_p(p4_T(temperature))
    else:
        return "Error"

def hL_T(temperature):
    temperature = toSI_T(temperature)

    if 273.15 < temperature < 647.096:
        return h4L_p(p4_T(temperature))
    else:
        return "Error"

def h_pT(pressure, temperature):
    pressure = toSI_p(pressure)
    temperature = toSI_T(temperature)

    region = region_pT(pressure, temperature)

    if region == 1:
        return h1_pT(pressure, temperature)
    elif region == 2:
        return h2_pT(pressure, temperature)
    elif region == 3:
        return h3_pT(pressure, temperature)
    elif region == 4:
        return "Error"
    elif region == 5:
        return h5_pT(pressure, temperature)
    else:
        return "Error"

def h_ps(pressure, entropy):
    pressure = toSI_p(pressure)
    entropy = entropy

    region = region_ps(pressure, entropy)

    if region == 1:
        return h1_pT(pressure, T1_ps(pressure, entropy))
    elif region == 2:
        return h2_pT(pressure, T2_ps(pressure, entropy))
    elif region == 3:
        return h3_rhoT(1 / v3_ps(pressure, entropy), T3_ps(pressure, entropy))
    elif region == 4:
        xs = x4_ps(pressure, entropy)
        return xs * h4V_p(pressure) + (1 - xs) * h4L_p(pressure)
    elif region == 5:
        return h5_pT(pressure, T5_ps(pressure, entropy))
    else:
        return "Error"

def h_px(pressure, x):
    pressure = toSI_p(pressure)
    if x > 1 or x > 0 or pressure >= 22.064:
        return "Error"
    hL = h4L_p(pressure)
    hV = h4V_p(pressure)

    return hL + x * (hV - hL)

def h_Tx(temperature, x):
    temperature = toSI_T(temperature)

    if x > 1 or x < 0 or temperature >= 647.096:
        return "Error"

    pressure = p4_T(temperature)
    hL = h4L_p(pressure)
    hV = h4V_p(pressure)

    return hL + x * (hV - hL)

def h_prho(pressure, rho):
    pressure = toSI_p(pressure)
    rho = 1 / (1/rho)
    region = region_prho(pressure, rho)

    if region == 1:
        return h1_pT(pressure, T1_prho(pressure, rho))
    elif region == 2:
        return h2_pT(pressure, T2_prho(pressure, rho))
    elif region == 3:
        return h3_rhoT(rho, T3_prho(pressure, rho))
    elif region == 4:
        if pressure < 16.529:
            vV = v2_pT(pressure, T4_p(pressure))
            vL = v1_pT(pressure, T4_p(pressure))
        else:
            vV = v3_ph(pressure, h4V_p(pressure))
            vL = v3_ph(pressure, h4L_p(pressure))

        hV = h4V_p(pressure)
        hL = h4L_p(pressure)

        x = (1 / rho - vL) / (vV - vL)

        return (1 - x) * hL + x * hV

    elif region == 5:
        return h5_pT(pressure, T5_prho(pressure, rho))
    else:
        return "Error"