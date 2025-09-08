import matplotlib.pyplot as plt
import numpy as np
import os

# ----------------------------
# Función que genera los puntos de la curva de Koch
# ----------------------------
def koch_curve(p1, p2, iteraciones):
    """
    Genera los puntos de la curva de Koch entre dos puntos.
    p1, p2 : extremos del segmento (x, y)
    iteraciones : nivel de detalle
    """
    if iteraciones == 0:
        # Caso base: devolvemos la línea recta
        return [p1, p2]
    else:
        # Convertimos a arrays para facilitar cálculos
        p1, p2 = np.array(p1), np.array(p2)
        
        # Vector de todo el segmento
        delta = p2 - p1

        # Dividimos en 3 partes
        pA = p1 + delta / 3
        pB = p1 + 2 * delta / 3

        # Punto del triángulo equilátero hacia afuera
        angulo = np.pi / 3  # 60 grados
        rotacion = np.array([[np.cos(angulo), -np.sin(angulo)],
                             [np.sin(angulo),  np.cos(angulo)]])
        pC = pA + rotacion.dot(delta / 3)

        # Recursividad: construimos en cada lado
        return (koch_curve(p1, pA, iteraciones - 1)[:-1] +
                koch_curve(pA, pC, iteraciones - 1)[:-1] +
                koch_curve(pC, pB, iteraciones - 1)[:-1] +
                koch_curve(pB, p2, iteraciones - 1))

# ----------------------------
# Función que genera el copo completo
# ----------------------------
def koch_snowflake(iteraciones):
    # Triángulo equilátero inicial (3 puntos)
    p1 = [0, 0]
    p2 = [1, 0]
    p3 = [0.5, np.sin(np.pi/3)]  # altura del triángulo

    # Generamos los 3 lados del triángulo
    lado1 = koch_curve(p1, p2, iteraciones)[:-1]
    lado2 = koch_curve(p2, p3, iteraciones)[:-1]
    lado3 = koch_curve(p3, p1, iteraciones)

    # Unimos todos los puntos
    return np.array(lado1 + lado2 + lado3)

# ----------------------------
# Generar y guardar imágenes
# ----------------------------
# Carpeta donde se guardarán las imágenes
output_dir = "koch_snowflake"
os.makedirs(output_dir, exist_ok=True)

for n in range(5):  # Iteraciones 0 a 4
    puntos = koch_snowflake(n)

    # Graficamos
    plt.figure(figsize=(6,6))
    plt.plot(puntos[:,0], puntos[:,1], color="black")
    plt.axis("equal")
    plt.axis("off")  # Quitamos ejes
    plt.title(f"Copo de Koch - Iteración {n}")

    # Guardamos la figura
    filename = os.path.join(output_dir, f"snowflake_iter_{n}.png")
    plt.savefig(filename, bbox_inches="tight", dpi=200)
    plt.close()

    print(f"Imagen guardada: {filename}")
