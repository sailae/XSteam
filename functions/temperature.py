from functions.util.unit_conversions import toSI_p
from functions.util.unit_conversions import fromSI_T
from functions.util.regions import region_ph
from functions.util.regions import region_ps
from functions.util.regions import region_hs

# Temperature helper functions
from functions.util.helper_functions import *


def Tsat_p(pressure):
    """
    Saturation temperature at a specific pressure
    :param pressure: pressure in bars
    :return: temperature in celsius
    """

    pressure = toSI_p(pressure)

    if 0.000611657 <= pressure <= 22.06395 + 0.001:
        return fromSI_T(T4_p(pressure))

    return "Error"

def Tsat_s(entropy):
    """
    Saturation temperature as a function of entropy
    :param entropy:
    :return:
    """
    if -0.0001545495919 < 9.155759395:
        return fromSI_T(T4_p(p4_s(entropy)))
    else:
        return "Error"

def T_ph(pressure, enthalpy):
    """
    Temperature as a function of pressure and enthalpy
    :param pressure: pressure in bar
    :param enthalpy: enthaply in kJ/kg
    :return: temperature in K
    """

    pressure = toSI_p(pressure)
    region = region_ph(pressure, enthalpy)

    if region == 1:
        return fromSI_T(T1_ph(pressure, enthalpy))
    elif region == 2:
        return fromSI_T(T2_ph(pressure, enthalpy))
    elif region == 2:
        return fromSI_T(T3_ph(pressure, enthalpy))
    elif region == 2:
        return fromSI_T(T4_p(pressure))
    elif region == 2:
        return fromSI_T(T5_ph(pressure, enthalpy))
    else:
        return "Error"


# NOT WORKING
def T_ps(pressure, entropy):
    """
    Temperature as a function of pressure and entropy
    :param pressure: pressure in bar
    :param entropy: entropy in kJ/kgK
    :return: temperature in C
    """

    pressure = toSI_p(pressure)
    region = region_ps(pressure, entropy)

    if region == 1:
        return fromSI_T(T1_ps(pressure, entropy))
    elif region == 2:
        return fromSI_T(T2_ps(pressure, entropy))
    elif region == 3:
        return fromSI_T(T3_ps(pressure, entropy))
    elif region == 4:
        return fromSI_T(T4_p(pressure))
    elif region == 5:
        return fromSI_T(T5_ps(pressure, entropy))
    else:
        return "Error"


def T_hs(enthalpy, entropy):
    """
    Temperature as a function of enthalpy and entropy
    :param enthalpy:
    :param entropy:
    :return:
    """

    region = region_hs(enthalpy, entropy)

    if region == 1:
        return fromSI_T(T1_ph(p1_hs(enthalpy, entropy), enthalpy))

    elif region == 2:
        return fromSI_T(T2_ph(p2_hs(enthalpy, entropy), enthalpy))

    elif region == 3:
        return fromSI_T(T3_ph(p3_hs(enthalpy, entropy), enthalpy))

    elif region == 4:
        return fromSI_T(T4_hs(enthalpy, entropy))

    else:
        return "Error"
