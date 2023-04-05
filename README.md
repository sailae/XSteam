# Documentation

This is a [XSteam made for Python](https://xsteam.sourceforge.net/). Here there are functions to calculate thermodynamic calculations for water or steam.

## Getting Started

Clone or download this repository to your personal computer and open the directory. You'll find a functions folder where all the thermodynamic functions are, main.py file, and .gitignore file. You can start building your program into the main.py or in the directory.

To call functions, you need first import the right functions.
```
from functions.{file name} import *
```
for example, to import the temperature functions, you need to import the temperature.py file from the functions folder.
```
from functions.temperature import *
```

## Units
The units are mostly SI-Units, you can find a detailed list below on each of the units
- temperature: $°C$
- pressure: $bar$
- enthalpy: $kJ/kg$
- specific volume: $m^3/kg$
- density: $kg/m^3$
- specific entropy: $kJ / kg K$
- specific internal energy: $kJ/kg$
- specific isobaric heat capacity: $kJ / kg °C$
- specific isochoric heat capacity: $kJ / kg °C$
- speed of sound: $m/s$
- dynamic viscosity: $Pas$
- thermal conductivity: $W / mK$
- surface tension: $N/m$ 

## Functions

### Density
- `rhoV_p(pressure)`
- `rhoL_p(pressure)`
- `rhoL_T(temperature)`
- `rhoV_T(temperature)`
- `rho_pT(pressure, temperature)`
- `rho_ph(pressure, enthalpy)`
- `rho_ps(pressure, entropy)`

### Enthalpy
- `hV_p(pressure)`
- `hL_p(pressure)`
- `hV_T(temperature)`
- `hL_T(temperature)`
- `h_pT(pressure, temperature)`
- `h_ps(pressure, entropy)`
- `h_px(pressure, vapour-fraction)`
- `h_Tx(temperature, vapour-graction)`
- `h_prho(pressure, density)`

### Kappa
- `Kappa_pT(pressure, temperature)`
- `Kappa_ph(pressure, enthalpy)`

### Prantl
- `Pr_pt(pressure, temperature)`
- `Pr_ph(pressure, enthalpy)`

### Pressure
- `psat_T(temperature)`
- `psat_s(entropy)`
- `p_hs(enthalpy, entropy)`
- `p_hrho(entalpy, density)`

### Specific Entropy
- `sV_p(pressure)`
- `sL_p(pressure)`
- `sV_T(temperature)`
- `sL_T(temperature)`
- `s_pT(pressure, temperature)`
- `s_ph(pressure, enthalpy)`

### Specific Internal Energy
- `uV_p(pressure)`
- `uL_p(pressure)`
- `uV_T(temperature)`
- `uL_T(temperature)`
- `u_pT(pressure, temperature)`
- `u_ph(pressure, enthalpy)`
- `u_ps(pressure, entropy)`

### Specific Isobaric Heat Capacity
- `CpV_p(pressure)`
- `CpL_p(pressure)`
- `CpV_T(temperature)`
- `CpL_T(temperature)`
- `Cp_pT(pressure, temperature)`
- `Cp_ph(pressure, enthalpy)`
- `Cp_ps(pressure, entropy)`

### Specific Isochoric Heat Capacity
- `CvV_p(pressure)`
- `CvL_p(pressure)`
- `CvL_T(temperature)`
- `CvV_T(temperature)`
- `Cv_pT(pressure, temperature)`
- `Cv_ph(pressure, enthalpy)`
- `Cv_ps(pressure, entropy)`

### Specific Volume
- `vV_p(pressure)`
- `vL_p(pressure)`
- `vV_T(temperature)`
- `vL_T(temperature)`
- `v_pT(pressure, temperature)`
- `v_ph(pressure, enthalpy)`
- `v_ps(pressure, entropy)`

### Speed of Sound
- `wV_p(pressure)`
- `wL_p(pressure)`
- `wV_T(temperature)`
- `wL_T(temperature)`
- `w_pT(pressure, temperature)`
- `w_ph(pressure, enthalpy)`
- `w_ps(pressure, entropy)`

### Surface Tension
- `st_t(temperature)`
- `st_p(pressure)`

### Temperature
- `Tsat_s(entropy)`
- `Tsat_p(pressure)`
- `T_ph(pressure, enthalpy)`
- `T_ps(pressure, entropy)`
- `T_hs(enthalpy, entropy)`

### Thermal Conductivity
- `tcL_p(pressure)`
- `tcV_p(pressure)`
- `tcL_T(temperature)`
- `tcV_T(temperature)`
- `tc_pT(pressure, temperature)`
- `tc_ph(pressure, enthalpy)`
- `tc_hs(enthalpy, entropy)`

### Vapour Fraction
- `x_ph(pressure, enthalpy)`
- `x_ps(pressure, entropy)`

### Vapour Volume Fraction
- `vx_ph(pressure, enthalpy)`
- `vx_ps(pressure, entropy)`

### Viscosity
- `my_pT(pressure, temperature)`
- `my_ph(pressure, enthalpy)`