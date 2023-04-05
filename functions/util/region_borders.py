
def B23p_T(temperature):

  return 348.05185628969 - 1.1671859879975 * temperature + 0.0010192970039326 * temperature ** 2

def B23T_p(pressure):
    return 572.54459862746 + ((pressure - 13.91883977887) / 0.0010192970039326) ** 0.5

def p3sat_h(enthalpy):
    Ii = [0, 1, 1, 1, 1, 5, 7, 8, 14, 20, 22, 24, 28, 36]
    Ji = [0, 1, 3, 4, 36, 3, 0, 24, 16, 16, 3, 18, 8, 24]
    ni = [0.600073641753024, -9.36203654849857, 24.6590798594147, -107.014222858224, -91582131580576.8,
          -8623.32011700662, -23.5837344740032, 2.52304969384128E+17, -3.89718771997719E+18, -3.33775713645296E+22,
          35649946963.6328, -1.48547544720641E+26, 3.30611514838798E+18, 8.13641294467829E+37]
    h = enthalpy / 2600
    ps = 0

    for i in range(0, 13):
        ps += ni[i] * (h - 1.02) ** Ii[i] * (h - 0.608) ** Ji[i]

    return ps * 22

def p3sat_s(entropy):

    Ii = [0, 1, 1, 4, 12, 12, 16, 24, 28, 32]
    Ji = [0, 1, 32, 7, 4, 14, 36, 10, 0, 18]
    ni = [0.639767553612785, -12.9727445396014, -2.24595125848403E+15, 1774667.41801846, 7170793495.71538,
          -3.78829107169011E+17, -9.55586736431328E+34, 1.87269814676188E+23, 119254746466.473,
          1.10649277244882E+36]

    sigma = entropy / 5.2
    p = 0

    for i in range(0, 9):
        p += ni[i] * (sigma - 1.03) ** Ii[i] * (sigma - 0.699) ** Ji[i]

    return p * 22

def hB13_s(entropy):
  Ii = [0, 1, 1, 3, 5, 6]
  Ji = [0, -2, 2, -12, -4, -3]
  ni = [0.913965547600543, -4.30944856041991E-05, 60.3235694765419, 1.17518273082168E-18, 0.220000904781292, -69.0815545851641]
  sigma = entropy / 3.8
  eta = 0
  for i in range(0, 5):
    eta = eta + ni[i] * (sigma - 0.884) ** Ii[i] * (sigma - 0.864) ** Ji[i]
  return eta * 1700

def TB23_hs(enthalpy, entropy):
  Ii = [-12, -10, -8, -4, -3, -2, -2, -2, -2, 0, 1, 1, 1, 3, 3, 5, 6, 6, 8, 8, 8, 12, 12, 14, 14]
  Ji = [10, 8, 3, 4, 3, -6, 2, 3, 4, 0, -3, -2, 10, -2, -1, -5, -6, -3, -8, -2, -1, -12, -1, -12, 1]
  ni = [0.00062909626082981, -0.000823453502583165, 5.15446951519474E-08, -1.17565945784945, 3.48519684726192, -5.07837382408313E-12, -2.84637670005479, -2.36092263939673, 6.01492324973779, 1.48039650824546, 0.000360075182221907, -0.0126700045009952, -1221843.32521413, 0.149276502463272, 0.698733471798484, -0.0252207040114321, 0.0147151930985213, -1.08618917681849, -0.000936875039816322, 81.9877897570217, -182.041861521835, 2.61907376402688E-06, -29162.6417025961, 1.40660774926165E-05, 7832370.62349385]
  sigma = entropy / 5.3
  eta = enthalpy / 3000
  teta = 0

  for i in range(0, 24):
    teta = teta + ni[i] * (eta - 0.727) ** Ii(i) * (sigma - 0.864) ** Ji[i]

  return teta * 900