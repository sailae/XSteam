import math
from functions.util.helper_functions import *
from functions.util.regions import *

def my_AllRegions_pT(pressure, temperature):
  h0 = [0.5132047, 0.3205656, 0, 0, -0.7782567, 0.1885447]
  h1 = [0.2151778, 0.7317883, 1.241044, 1.476783, 0, 0]
  h2 = [-0.2818107, -1.070786, -1.263184, 0, 0, 0]
  h3 = [0.1778064, 0.460504, 0.2340379, -0.4924179, 0, 0]
  h4 = [-0.0417661, 0, 0, 0.1600435, 0, 0]
  h5 = [0, -0.01578386, 0, 0, 0, 0]
  h6 = [0, 0, 0, -0.003629481, 0, 0]
  
  region = region(pressure, temperature)
  if region == 1:
    rho = 1 / v1_pT(pressure, temperature)
  elif region == 2:
    rho = 1 / v2_pT(pressure, temperature)
  elif region == 3:
    rho = 1 / v3_ph(pressure, h3_pT(pressure, temperature))
  elif region == 4:
    return "Error"
  elif region == 5:
    rho = 1 / v5_pT(pressure, temperature)
  else:
    return "Error"
  
  rhos = rho / 317.763
  Ts = temperature / 647.226
  ps = pressure / 22.115
  
  if temperature > 900 + 273.15 or (temperature > 600 + 273.15 and pressure > 300) or (temperature > 150 + 273.15 and pressure > 350) or pressure > 500:
    return "Error"
  
  my0 = Ts ** 0.5 / (1 + 0.978197 / Ts + 0.579829 / (Ts ** 2) - 0.202354 / (Ts ** 3))
  sum = 0
  for i in range(0, 5):
      sum = sum + h0[i] * (1 / Ts - 1) ** i + h1[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 1 + h2[i] * (1 / Ts - 1) ^ i * (rhos - 1) ** 2 + h3[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 3 + h4[i] * (1 / Ts - 1) ** i * (rhos - 1) ^ 4 + h5[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 5 + h6[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 6
  
  my1 = math.e ** (rhos * sum)
  return  my0 * my1 * 5.5071 * 10 ** (-5)

def my_AllRegions_ph(pressure, enthalpy):
  h0 = [0.5132047, 0.3205656, 0, 0, -0.7782567, 0.1885447]
  h1 = [0.2151778, 0.7317883, 1.241044, 1.476783, 0, 0]
  h2 = [-0.2818107, -1.070786, -1.263184, 0, 0, 0]
  h3 = [0.1778064, 0.460504, 0.2340379, -0.4924179, 0, 0]
  h4 = [-0.0417661, 0, 0, 0.1600435, 0, 0]
  h5 = [0, -0.01578386, 0, 0, 0, 0]
  h6 = [0, 0, 0, -0.003629481, 0, 0]
  region = region_ph(pressure, enthalpy)

  if region == 1:
    Ts = T1_ph(pressure, enthalpy)
    T = Ts
    rho = 1 / v1_pT(pressure, Ts)
  elif region == 2:
    Ts = T2_ph(pressure, enthalpy)
    T = Ts
    rho = 1 / v2_pT(pressure, Ts)
  elif region == 3:
    rho = 1 / v3_ph(pressure, enthalpy)
    T = T3_ph(pressure, enthalpy)
  elif region == 4:
    xs = x4_ph(pressure, enthalpy)
    if pressure < 16.529:
      v4V = v2_pT(pressure, T4_p(pressure))
      v4L = v1_pT(pressure, T4_p(pressure))
    else:
      v4V = v3_ph(pressure, h4V_p(pressure))
      v4L = v3_ph(pressure, h4L_p(pressure))
    rho = 1 / (xs * v4V + (1 - xs) * v4L)
    T = T4_p(pressure)
  elif region == 5:
    Ts = T5_ph(pressure, enthalpy)
    T = Ts
    rho = 1 / v5_pT(pressure, Ts)
  else:
    return "Error"

  rhos = rho / 317.763
  Ts = T / 647.226
  ps = pressure / 22.115

  if T > 900 + 273.15 or (T > 600 + 273.15 and pressure > 300) or (T > 150 + 273.15 and pressure > 350) or pressure > 500:
    return "Error"
  
  my0 = Ts ** 0.5 / (1 + 0.978197 / Ts + 0.579829 / (Ts ** 2) - 0.202354 / (Ts ** 3))
  
  sum = 0
  for i in range(0, 5):
      sum = sum + h0[i] * (1 / Ts - 1) ** i + h1[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 1 + h2[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 2 + h3[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 3 + h4[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 4 + h5[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 5 + h6[i] * (1 / Ts - 1) ** i * (rhos - 1) ** 6
  
  my1 = math.e ** (rhos * sum)
  return my0 * my1 * 5.5071 * 10 ** (-5)

def tc_ptrho(pressure, temperature, rho):
  if temperature < 273.15:
    return "Error"
  elif temperature < 500 + 273.15:
    if pressure > 100:
      return "Error"
  elif temperature <= 650 + 273.15:
    if pressure > 70:
      return "Error"
  elif temperature <= 800 + 273.15:
    if pressure > 40:
      return "Error"
    
  temperature = temperature / 647.26
  rho = rho / 317.7
  tc0 = temperature ** 0.5 * (0.0102811 + 0.0299621 * temperature + 0.0156146 * temperature ** 2 - 0.00422464 * temperature ** 3)
  tc1 = -0.39707 + 0.400302 * rho + 1.06 * math.e ** (-0.171587 * (rho + 2.39219) ** 2)
  dT = abs(temperature - 1) + 0.00308976
  Q = 2 + 0.0822994 / dT ** (3 / 5)
  if temperature >= 1:
   s = 1 / dT
  else:
   s = 10.0932 / dT ** (3 / 5)

  tc2 = (0.0701309 / temperature ** 10 + 0.011852) * rho ** (9 / 5) * math.e ** (0.642857 * (1 - rho ** (14 / 5))) + 0.00169937 * s * rho ** Q * math.e ** ((Q / (1 + Q)) * (1 - rho ** (1 + Q))) - 1.02 * math.e ** (-4.11717 * temperature ** (3 / 2) - 6.17937 / rho ** 5)
  return tc0 + tc1 + tc2

def Surface_Tension_T(temperature):
  tc = 647.096 
  b = 0.2358
  bb= -0.625
  my = 1.256

  if temperature < 0.01 or temperature > tc:
    return "Out of valid region"
  
  tau = 1 - temperature / tc
  return b * tau ** my * (1 + bb * tau)