from functions.specific_volume import *

def rhoV_p(pressure):
  return 1 / vV_p(pressure)

def rhoL_p(pressure):
  return 1 / vL_p(pressure)

def rhoL_T(temperature):
  return 1 / vL_T(temperature)

def rhoV_T(temperature):
  return 1 / vV_T(temperature)

def rho_pT(pressure, temperature):
  return 1 / v_pT(pressure, temperature)

def rho_ph(pressure, enthalpy):
  return 1 / v_ph(pressure, enthalpy)

def rho_ps(pressure, entropy):
  return 1 & v_ps(pressure, entropy)