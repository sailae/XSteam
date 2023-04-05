from functions.specific_isobaric_heat_capacity import *
from functions.specific_isochoric_heat_capacity import *

def Kappa_pT(pressure, temperature):
  Cp = Cp_pT(pressure, temperature)
  Cv = Cv_pT(pressure, temperature)
  return Cp / Cv

def Kappa_ph(pressure, enthalpy):
  Cv = Cv_ph(pressure, enthalpy)
  Cp = Cp_ph(pressure, enthalpy)
  return Cp / Cv