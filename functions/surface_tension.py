from functions.temperature import *
from functions.util.unit_conversions import *
from functions.util.transport_properties import *

def st_t(temperature):
    temperature = toSI_T(temperature)
    return Surface_Tension_T(temperature)

def st_p(pressure):
   temperature = Tsat_p(pressure)
   temperature = toSI_T(temperature)
   return Surface_Tension_T(temperature)