import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las funciones por tramos
def funcion(x):
    if np.isscalar(x):
        if 0 <= x <= 0.45:
            return -2.58 * x**3 + 0.02 * x**2 + 0.26 * x + 1.97
        elif 0.44 <= x <= 2.06:
            return -0.08 * x**6 + 0.04 * x**5 + 1.78 * x**4 - 5.04 * x**3 + 4.25 * x**2 - 0.88 * x + 1.79
        elif 2.06 <= x <= 2.25:
            return -5.24 * x**2 + 21.2 * x - 20.06
        elif 2.21 <= x <= 4.72:
            return -0.01 * x**3 + 0.29 * x**2 - 1.84 * x + 3.95
        elif 4.7 <= x <= 4.95:
            return -11.14 * x**2 + 109.96 * x - 270.17
        elif 4.93 <= x <= 5.32:
            return -1.02 * x**3 + 12.48 * x**2 - 48.08 * x + 57.1
        elif 5.31 <= x <= 5.59:
            return -28.11 * x**3 + 452.4 * x**2 - 2426.46 * x + 4338.2
        elif 5.58 <= x <= 5.93:
            return 368.32 * x**5 - 10447.75 * x**4 + 118484.82 * x**3 - 671507.35 * x**2 + 1901876.49 * x - 2153486.97
        elif 5.92 <= x <= 7.09:
            return 0.66 * x**2 - 8.18 * x + 25.931
        elif 7.09 <= x <= 7.37:
            return -35.8 * x**3 + 766.23 * x**2 - 5467.2 * x + 13005.783
        elif 7.34 <= x <= 7.85:
            return -1.34 * x**2 + 19.41 * x - 69.63
        elif 7.85 <= x <= 8.2:
            return -1.7 * x**2 + 27.47 * x - 110.7
        elif 8.2 <= x <= 8.37:
            return -9.78 * x**2 + 160.59 * x - 658.979
        else:
            return np.nan  # Fuera de los límites
    else:
        return np.array([funcion(xi) for xi in x])  # Para arreglos

# Crear listas para almacenar x e y por tramos
x_vals = []
y_vals = []

# Definir los intervalos de las funciones para asegurarnos de que se concatenen correctamente
intervalos = [
    (0, 0.45), (0.44, 2.06), (2.06, 2.25), (2.21, 4.72), (4.7, 4.95),
    (4.93, 5.32), (5.31, 5.59), (5.58, 5.93), (5.92, 7.09), (7.09, 7.37),
    (7.34, 7.85), (7.85, 8.2), (8.2, 8.37)
]

# Generar los valores de x e y para cada intervalo
for intervalo in intervalos:
    x_tramo = np.linspace(intervalo[0], intervalo[1], 100)
    y_tramo = funcion(x_tramo)
    x_vals.append(x_tramo)
    y_vals.append(y_tramo)

# Concatenar todos los tramos
x_total = np.concatenate(x_vals)
y_total = np.concatenate(y_vals)

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la función original
ax.plot(x_total, y_total, np.zeros_like(x_total), 'b-')

# Crear la malla de revolución sobre el eje X
theta = np.linspace(0, 2 * np.pi, 100)
theta_grid, y_grid = np.meshgrid(theta, y_total)

# Rotación sobre el eje X
x_grid = np.tile(x_total, (100, 1)).T  # Repetir x_total
z_grid = y_grid * np.sin(theta_grid)
y_grid = y_grid * np.cos(theta_grid)

# Graficar la superficie de revolución
ax.plot_surface(x_grid, y_grid, z_grid, color='b', alpha=0.5)

# Ajustar los ejes para mejorar la visualización
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Sólido de Revolución - Reina")

# Mostrar la figura
plt.show()