from functions.temperature import *
from functions.specific_volume import *
from functions.util.transport_properties import *
from functions.pressure import *

def tcL_p(pressure):
  temperature = Tsat_p(pressure)
  v = vL_p(pressure)
  pressure = toSI_p(pressure)
  temperature = toSI_T(temperature)
  return tc_ptrho(pressure, temperature, 1 / v)

def tcV_p(pressure):
  temperature = Tsat_p(pressure)
  v = vV_p(pressure)
  pressure = toSI_p(pressure)
  temperature = toSI_T(temperature)
  return tc_ptrho(pressure, temperature, 1 / v)

def tcL_T(temperature):
  pressure = psat_T(temperature)
  v = vL_T(temperature)
  pressure = toSI_p(pressure)
  temperature = toSI_T(temperature)
  return tc_ptrho(pressure, temperature, 1 / v)

def tcV_T(temperature):
  pressure = psat_T(temperature)
  v = vV_T(temperature)
  pressure = toSI_p(pressure)
  temperature = toSI_T(temperature)
  return tc_ptrho(pressure, temperature, 1 / v)

def tc_pT(pressure, temperature):
  v = v_pT(pressure, temperature)
  pressure = toSI_p(pressure)
  temperature = toSI_T(temperature)
  return tc_ptrho(pressure, temperature, 1 / v)

def tc_ph(pressure, enthalpy):
  v = v_ph(pressure, enthalpy)
  temperature = T_ph(pressure, enthalpy)
  pressure = toSI_p(pressure)
  temperature = toSI_T(temperature)
  return tc_ptrho(pressure, temperature, 1 / v)

def tc_hs(enthalpy, entropy):
  pressure = p_hs(enthalpy, entropy)
  v = v_ph(pressure, enthalpy)
  temperature = T_ph(pressure, enthalpy)
  pressure = toSI_p(pressure)
  temperature = toSI_T(temperature)
  return tc_ptrho(pressure, temperature, 1 / v)