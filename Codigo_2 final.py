# ==============================================
# Sistema de Gestión de Estudiantes - Versión Completa
# ==============================================

estudiantes = []

def registrar_estudiante():
    print("\n📝 --- Registrar Nuevo Estudiante ---")
    nombre = input("Ingrese el nombre completo: ")
    edad = input("Ingrese la edad: ")
    carrera = input("Ingrese la carrera: ")
    
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    estudiantes.append(estudiante)
    print(f"✅ Estudiante '{nombre}' registrado exitosamente.")

def ver_lista():
    print("\n📋 --- Lista de Estudiantes ---")
    if len(estudiantes) == 0:
        print("⚠️ No hay estudiantes registrados.")
        return
    
    for i, est in enumerate(estudiantes, 1):
        print(f"\nEstudiante #{i}")
        print(f"  Nombre:  {est['nombre']}")
        print(f"  Edad:    {est['edad']} años")
        print(f"  Carrera: {est['carrera']}")

def buscar_estudiante():
    print("\n🔍 --- Buscar Estudiante ---")
    busqueda = input("Ingrese el nombre a buscar: ").lower()
    encontrados = []
    
    for est in estudiantes:
        if busqueda in est["nombre"].lower():
            encontrados.append(est)
    
    if len(encontrados) > 0:
        print(f"\n✅ Se encontraron {len(encontrados)} resultado(s):")
        for est in encontrados:
            print(f"  - {est['nombre']} | {est['edad']} años | {est['carrera']}")
    else:
        print("❌ No se encontró ningún estudiante con ese nombre.")

def mostrar_menu():
    print("\n" + "="*45)
    print("      SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("="*45)
    print(" 1. Registrar nuevo estudiante")
    print(" 2. Ver lista completa de estudiantes")
    print(" 3. Buscar estudiante por nombre")
    print(" 4. Salir del sistema")
    print("="*45)

def main():
    print("\n🎉 ¡Bienvenido al Sistema de Gestión de Estudiantes!")
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción [1-4]: ")
        
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            ver_lista()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            print("\n👋 Gracias por usar nuestro sistema. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Por favor intente nuevamente.")

if __name__ == "__main__":
    main()
