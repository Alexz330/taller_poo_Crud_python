from Alumno import Alumno
from Curso import Curso
from colorama import init, Fore, Style

# Inicializar colorama para habilitar el soporte de colores en la consola
init(autoreset=True)

def mostrar_menu():
    print("\n--- Menú ---")
    print(f"{Fore.YELLOW}1. Mostrar cursos de un alumno{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}2. Asignar curso a un alumno{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}3. Actualizar nombre de un alumno{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}4. Eliminar curso de un alumno{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}5. Salir{Style.RESET_ALL}")

def main():
    # Creamos algunos cursos y alumnos
    curso1 = Curso("Matemáticas", "Profesor Martínez")
    curso2 = Curso("Historia", "Profesora Gómez")
    curso3 = Curso("Inglés", "Profesor Johnson")

    alumno1 = Alumno("Juan", "2021001")
    alumno2 = Alumno("María", "2021002")

    alumno1.asignar_curso(curso1)
    alumno1.asignar_curso(curso2)
    alumno2.asignar_curso(curso2)
    alumno2.asignar_curso(curso3)

    # Interfaz de consola
    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            if nombre_alumno == alumno1.nombre:
                alumno1.mostrar_cursos()
            elif nombre_alumno == alumno2.nombre:
                alumno2.mostrar_cursos()
            else:
                print(f"{Fore.RED}Alumno no encontrado.{Style.RESET_ALL}")
        elif opcion == "2":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            nombre_curso = input("Ingrese el nombre del curso: ")
            catedratico_curso = input("Ingrese el nombre del catedrático: ")
            curso_nuevo = Curso(nombre_curso, catedratico_curso)
            if nombre_alumno == alumno1.nombre:
                alumno1.asignar_curso(curso_nuevo)
                print(f"{Fore.GREEN}Curso {nombre_curso} asignado a {alumno1.nombre}.{Style.RESET_ALL}")
            elif nombre_alumno == alumno2.nombre:
                alumno2.asignar_curso(curso_nuevo)
                print(f"{Fore.GREEN}Curso {nombre_curso} asignado a {alumno2.nombre}.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Alumno no encontrado.{Style.RESET_ALL}")
        elif opcion == "3":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            if nombre_alumno == alumno1.nombre:
                alumno1.actualizar_nombre(nuevo_nombre)
                print(f"{Fore.GREEN}Nombre actualizado para {nombre_alumno}.{Style.RESET_ALL}")
            elif nombre_alumno == alumno2.nombre:
                alumno2.actualizar_nombre(nuevo_nombre)
                print(f"{Fore.GREEN}Nombre actualizado para {nombre_alumno}.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Alumno no encontrado.{Style.RESET_ALL}")
        elif opcion == "4":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            nombre_curso = input("Ingrese el nombre del curso a eliminar: ")
            if nombre_alumno == alumno1.nombre:
                alumno1.eliminar_curso(nombre_curso)
            elif nombre_alumno == alumno2.nombre:
                alumno2.eliminar_curso(nombre_curso)
            else:
                print(f"{Fore.RED}Alumno no encontrado.{Style.RESET_ALL}")
        elif opcion == "5":
            print(f"{Fore.YELLOW}¡Hasta luego!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, seleccione una opción válida.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
