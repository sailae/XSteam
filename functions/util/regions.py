import math
from functions.util.helper_functions import *

# REGIONS AS THE FUNCTION OF PT

def region_pT(pressure, temperature):
    if temperature > 1073.15 and pressure < 10 and temperature < 2273.15 and pressure > 0.000611:
        return 5
    elif temperature <= 1073.15 and temperature > 273.15 and pressure <= 100 and pressure > 0.000611:
        if temperature > 623.15:
            if pressure > B23p_T(temperature):
                if temperature <  647.096:
                    ps = p4_T(temperature)
                    if abs(pressure - ps) < 10 ** (-5):
                        return 4
                    else:
                        return 3
                else:
                    return 3
            else:
                return 2
        else:
            ps = p4_T(temperature)
            if abs(pressure - ps) < 10 ** (-5):
                return 4
            elif pressure > ps:
                return 1
            else:
                return 2
    else:
        return 0

#  REGIONS AS THE FUNCTION OF PH

def region_ph(pressure, enthalpy):
    if pressure < 0.000611657 or pressure > 100:
        return 0

    if enthalpy < 0.963 * pressure + 2.2:
        if enthalpy < h1_pT(pressure, 273.15):
            return 0

    if pressure < 16.5292:
        Ts = T4_p(pressure)
        hL = 109.6635 * math.log(pressure) + 40.3481 * pressure + 734.58

        if abs(enthalpy - hL) < 100:
            hL = h1_pT(pressure, Ts)

        if enthalpy <= hL:
            return 1

        hV = 45.1768 * math.log(pressure) - 20.158 * pressure + 2804.4

        if abs(enthalpy - hV) < 50:
            hV = h2_pT(pressure, Ts)

        if enthalpy < hV:
            return 4

        if enthalpy < 4000:
            return 2

        h45 = h2_pT(pressure, 1073.15)

        if enthalpy <= h45:
            return 2

        if pressure > 10:
            return 0

        h_5u = h5_pT(pressure, 2273.15)

        if enthalpy < h_5u:
            return 5

        return 0

    else:
        if enthalpy < h1_pT(pressure, 623.15):
            return 1

        if enthalpy < h2_pT(pressure, B23T_p(pressure)):
            if pressure < p3sat_h(enthalpy):
                return 3
            else:
                return 4

    if enthalpy < h2_pT(pressure, 1073.15):
        return 2

    return 0

# REGIONS AS THE FUNCTION OF PS

def region_ps(pressure, entropy):

    if pressure < 0.000611657 or entropy < 0 or entropy > s5_pT(pressure, 2273.15):
        return 0

    if entropy > s2_pT(pressure, 1073.15):
        if pressure <= 10:
            return 5
        else:
            return 0

    if pressure > 16.529:
        ss = s2_pT(pressure, B23T_p(pressure))
    else:
        ss = s2_pT(pressure, T4_p(pressure))

    if entropy > ss:
        return 2

    ss = s1_pT(pressure, 623.15)

    if 16.529 and entropy > ss:
        if pressure > p3sat_s(entropy):
            return 3
        else:
            return 4

    if pressure < 16.529 and entropy > s1_pT(pressure, T4_p(pressure)):
        return 4

    if pressure > 0.000611657 and entropy > s1_pT(pressure, 273.15):
        return 1

    return 1

# REGIONS AS THE FUNCTIONS OF HS

def region_hs(enthalpy, entropy):

    if entropy < -0.0001545495919:
        return 0

    hMin = (((-0.0415878 - 2500.89262) / (-0.00015455 - 9.155759)) * entropy)

    if entropy < 9.155759395 and enthalpy < hMin:
        return 0

    if -0.0001545495919 <= entropy <= 3.77828134:
        if enthalpy < h4_s(entropy):
            return 4

        elif entropy < 3.397782955:
            TMax = T1_ps(100, entropy)
            hMax = h1_pT(100, TMax)

            if enthalpy < hMax:
                return 1

            else:

                return 0

        else:

            hB = hB13_s(entropy)

            if enthalpy < hB:
                return 1

            TMax = T3_ps(100, entropy)
            vmax = v3_ps(100, entropy)
            hMax = h3_rhoT(1 / vmax, TMax)

            if enthalpy < hMax:
                return 3

            else:
                return 0


    if 5.260578707 <= entropy <= 11.9212156897728:

        TMin = T2_ps(0.000611, entropy)
        hMin = h2_pT(0.000611, TMin)

        hMax = -0.07554022 * entropy ** 4 + 3.341571 * entropy ** 3 - 55.42151 * entropy ** 2 + 408.515 * entropy + 3031.338

        if hMin < enthalpy < hMax:
            return 2

        else:
            return 0

    hV = h4_s(entropy)

    if enthalpy < hV:
        return 4

    if entropy < 6.04048367171238:
        TMax = T2_ps(100, entropy)
        hMax = h2_pT(100, TMax)
    else:
        hMax = -2.988734 * entropy ** 4 + 121.4015 * entropy ** 3 - 1805.15 * entropy ** 2 + 11720.16 * entropy - 23998.33

        if enthalpy < hMax:
            return 2

        else:
            return 0

    if 3.778281134 <= entropy <= 4.41202148223476:
        hL = h4_s(entropy)
        if hL > enthalpy:
            return 4

        TMax = T3_ps(100, entropy)
        vmax = v3_ps(100, entropy)
        hMax = h3_rhoT(1 / vmax, TMax)

        if enthalpy < hMax:
            return 3
        else:
            return 0

    if 4.41202148223476 <= entropy <= 5.260578707:
        hV = h4_s(entropy)
        if enthalpy < hV:
            return 4
        if entropy <= 5.048096828:
            TMax = T3_ps(100, entropy)
            vmax = v3_ps(100, entropy)
            hMax = h3_rhoT(1 / vmax, TMax)

            if enthalpy < hMax:
                return 3
            else:
                return 0
        else:
            if enthalpy > 2812.942061:
                if entropy > 5.09796573397125:
                    TMax = T2_ps(100, entropy)
                    hMax = h2_pT(100, TMax)
                    if enthalpy < hMax:
                        return 2
                    else:
                        return 0
                else:
                    return 0
            if enthalpy < 2563.592004:
                return 3

            if p2_hs(enthalpy, entropy) > B23p_T(TB23_hs(enthalpy, entropy)):
                return 3
            else:
                return 2

    return "Error"

# REGIONS AS THE FUNCTION OF PRHO

def region_prho(pressure, rho):
    v = 1 / rho
    if pressure < 0.000611657 or pressure > 100:
        return 0
    if pressure < 16.5292:
        if v < v1_pT(pressure, 273.15):
            return 0
        if v <= v1_pT(pressure, T4_p(pressure)):
            return 1
        if v <= v2_pT(pressure, T4_p(pressure)):
            return 4
        if v <= v2_pT(pressure, 1073.15):
            return 2
        if pressure > 10:
            return 0
        if v <= v5_pT(pressure, 2073.15):
            return 5
        else:
            if v < v1_pT(pressure, 273.15):
                return 0
            if v < v1_pT(pressure, 623.15):
                return 1
            if v < v2_pT(pressure, B23T_p(pressure)):
                if pressure > 22.064:
                    return 3
                if v < v3_ph(pressure, h4L_p(pressure)) or v > v3_ph(pressure, h4V_p(pressure)):
                    return 3
                else:
                    return 4
            if v < v2_pT(pressure, 1073.15):
                return 2
        
        return 0