from functions.specific_isobaric_heat_capacity import *
from functions.viscosity import *
from functions.thermal_conductivity import *

def Pr_pt(pressure, temperature):
    Cp = Cp_pT(pressure, temperature)
    my = my_pT(pressure, temperature)
    tc = tc_pT(pressure, temperature)
    return Cp * 1000 * my / tc

def Pr_ph(pressure, enthalpy):
  Cp = Cp_ph(pressure, enthalpy)
  my = my_ph(pressure, enthalpy)
  tc = tc_ph(pressure, enthalpy)
  return Cp * 1000 * my / tc