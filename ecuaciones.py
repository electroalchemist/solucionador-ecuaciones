def leer_numero(nombre):
    """Pide un número al usuario hasta que escriba uno válido."""
    while True:
        try:
            return float(input(f"Ingresa el coeficiente {nombre}: "))
        except ValueError:
            print("Valor no válido, intenta de nuevo.")


def resolver_sistema(a, b, c, d, e, f):
    """
    Resuelve el sistema:
        ax + by = c
        dx + ey = f
    Devuelve (x, y), o None si no hay solución única.
    """
    det = a * e - b * d
    if det == 0:
        return None
    det_x = c * e - b * f
    det_y = a * f - c * d
    return det_x / det, det_y / det


def main():
    print("Un sistema de ecuaciones 2x2 se escribe:")
    print("  ax + by = c")
    print("  dx + ey = f\n")

    a, b, c, d, e, f = (leer_numero(n) for n in "abcdef")

    resultado = resolver_sistema(a, b, c, d, e, f)

    if resultado is None:
        print("\nEl determinante es 0: el sistema no tiene solución única")
        print("(no tiene solución o tiene infinitas).")
    else:
        x, y = resultado
        print(f"\nSolución: x = {x:.4g}, y = {y:.4g}")


if __name__ == "__main__":
    main()