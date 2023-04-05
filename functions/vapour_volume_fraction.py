from functions.util.helper_functions import *
from functions.util.unit_conversions import *

def vx_ph(pressure, enthalpy):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            vL = v1_pT(pressure, T4_p(pressure))
            vV = v2_pT(pressure, T4_p(pressure))
        else:
            vL = v3_ph(pressure, h4L_p(pressure))
            vV = v3_ph(pressure, h4V_p(pressure))
        xs = x4_ph(pressure, enthalpy)
        return xs * vV / (xs * vV + (1 - xs) * vL)
    else:
        return "Error"


def vx_ps(pressure, entropy):
    pressure = toSI_p(pressure)
    if 0.000611657 < pressure < 22.06395:
        if pressure < 16.529:
            vL = v1_pT(pressure, T4_p(pressure))
            vV = v2_pT(pressure, T4_p(pressure))
        else:
            vL = v3_ph(pressure, h4L_p(pressure))
            vV = v3_ph(pressure, h4V_p(pressure))

        xs = x4_ps(pressure, entropy)
        return xs * vV / (xs * vV + (1 - xs) * vL)

    else:
        return "Error"