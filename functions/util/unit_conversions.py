def toSI_p(pressureBAR):
    """
    Convert from bar to MPa
    :param pressureBAR: pressure in bars
    :return: pressure in MPa
    """
    return pressureBAR / 10

def fromSI_p(pressureMPa):
    """
    Convert from MPa to bar
    :param pressureMPa: pressure in MPa
    :return: pressure in bars
    """

    return pressureMPa * 10

def toSI_T(temperatureK):
    """
    Convert from C to K
    :param temperatureK: temperature in K
    :return: temperature in C
    """
    return temperatureK + 273.15

def fromSI_T(temperatureC):
    """
    Convert from C to K
    :param temperatureC: temperature in K
    :return: temperature in C
    """
    return temperatureC - 273.15