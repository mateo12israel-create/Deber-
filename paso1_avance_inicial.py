# ============================================================
# SISTEMA DE GESTIÓN DE ESTUDIANTES
# Paso 1: Avance inicial — Entorno configurado y menú base
# ------------------------------------------------------------
# Lenguaje : Python 3.x
# IDE      : Visual Studio Code
# Control  : Git + GitHub
# Estado   : Avance inicial (las funciones se desarrollan en el Paso 2)
# ============================================================

# Lista que almacenará a los estudiantes (se llena en el Paso 2).
# Cada estudiante se guardará como un diccionario:
# {"nombre": "...", "edad": ..., "carrera": "..."}
estudiantes = []


def mostrar_menu():
    """Muestra el menú principal del sistema con las 4 opciones."""
    print("\n" + "=" * 45)
    print("       SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("=" * 45)
    print("  1. Registrar nuevo estudiante")
    print("  2. Ver lista de estudiantes")
    print("  3. Buscar estudiante por nombre")
    print("  4. Salir del sistema")
    print("=" * 45)


# ------------------------------------------------------------
# Programa principal (avance inicial del Paso 1)
# ------------------------------------------------------------
print("¡Bienvenido/a al Sistema de Gestión de Estudiantes!")

# Bucle que mantiene el menú activo hasta que el usuario elija salir.
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    # Estructura condicional que dirige al usuario según su elección.
    # En el Paso 1 las opciones 1, 2 y 3 quedan como avance pendiente.
    if opcion == "1":
        print("→ [AVANCE] Opción 1: Registrar estudiante. Pendiente de desarrollo en el Paso 2.")
    elif opcion == "2":
        print("→ [AVANCE] Opción 2: Ver lista de estudiantes. Pendiente de desarrollo en el Paso 2.")
    elif opcion == "3":
        print("→ [AVANCE] Opción 3: Buscar estudiante. Pendiente de desarrollo en el Paso 2.")
    elif opcion == "4":
        # break termina el bucle y finaliza el programa.
        print("👋 Gracias por usar el sistema. ¡Hasta pronto!")
        break
    else:
        # Se repite el menú si la opción no es válida.
        print("❌ Opción no válida. Ingrese un número del 1 al 4.")
