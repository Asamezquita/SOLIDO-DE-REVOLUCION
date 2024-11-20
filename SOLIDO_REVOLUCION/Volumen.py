import numpy as np
from scipy.integrate import quad

# Definir las funciones en sus respectivos intervalos
def g(x):
    if 0 <= x <= 0.45:
        return -2.58 * x**3 + 0.02 * x**2 + 0.26 * x + 1.97
    return np.nan

def p(x):
    if 0.44 <= x <= 2.06:
        return -0.08 * x**6 + 0.04 * x**5 + 1.78 * x**4 - 5.04 * x**3 + 4.25 * x**2 - 0.88 * x + 1.79
    return np.nan

def t(x):
    if 2.06 <= x <= 2.25:
        return -5.24 * x**2 + 21.2 * x - 20.06
    return np.nan

def s_2(x):
    if 2.21 <= x <= 4.72:
        return -0.01 * x**3 + 0.29 * x**2 - 1.84 * x + 3.95
    return np.nan

def h_3(x):
    if 4.7 <= x <= 4.95:
        return -11.14 * x**2 + 109.96 * x - 270.17
    return np.nan

def f_3(x):
    if 4.93 <= x <= 5.32:
        return -1.02 * x**3 + 12.48 * x**2 - 48.08 * x + 57.1
    return np.nan

def p_3(x):
    if 5.31 <= x <= 5.59:
        return -28.11 * x**3 + 452.4 * x**2 - 2426.46 * x + 4338.2
    return np.nan

def q_3(x):
    if 5.58 <= x <= 5.93:
        return 368.32 * x**5 - 10447.75 * x**4 + 118484.82 * x**3 - 671507.35 * x**2 + 1901876.49 * x - 2153486.97
    return np.nan

def r_3(x):
    if 5.92 <= x <= 7.09:
        return 0.66 * x**2 - 8.18 * x + 25.931
    return np.nan

def t_1(x):
    if 7.09 <= x <= 7.37:
        return -35.8 * x**3 + 766.23 * x**2 - 5467.2 * x + 13005.783
    return np.nan

def s_3(x):
    if 7.34 <= x <= 7.85:
        return -1.34 * x**2 + 19.41 * x - 69.63
    return np.nan

def t_3(x):
    if 7.85 <= x <= 8.2:
        return -1.7 * x**2 + 27.47 * x - 110.7
    return np.nan

def g_4(x):
    if 8.2 <= x <= 8.37:
        return -9.78 * x**2 + 160.59 * x - 658.979
    return np.nan

# Lista de funciones y sus intervalos
functions = [
    ("g", g, 0, 0.45),
    ("p", p, 0.44, 2.06),
    ("t", t, 2.06, 2.25),
    ("s_2", s_2, 2.21, 4.72),
    ("h_3", h_3, 4.7, 4.95),
    ("f_3", f_3, 4.93, 5.32),
    ("p_3", p_3, 5.31, 5.59),
    ("q_3", q_3, 5.58, 5.93),
    ("r_3", r_3, 5.92, 7.09),
    ("t_1", t_1, 7.09, 7.37),
    ("s_3", s_3, 7.34, 7.85),
    ("t_3", t_3, 7.85, 8.2),
    ("g_4", g_4, 8.2, 8.37)
]

# Función para calcular el volumen
def volume_of_revolution(func, a, b):
    integral, _ = quad(lambda x: func(x) ** 2, a, b)  # Sin pi aquí
    return integral

# Calcular el volumen total
total_integral = 0
for name, func, a, b in functions:
    integral_value = volume_of_revolution(func, a, b)
    total_integral += integral_value
    print(f"Función {name} en el intervalo [{a}, {b}]: Integral = {integral_value:.4f}")

# Imprimir el valor total de la sumatoria antes de multiplicar por pi
print(f"\nValor total de la sumatoria de las integrales: {total_integral:.4f}")

# Multiplicar el total de las integrales por pi para obtener el volumen total
total_volume = np.pi * total_integral
print(f"Volumen total del sólido de revolución: {total_volume:.4f}")