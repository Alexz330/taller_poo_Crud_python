class Alumno:
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet
        self.cursos = []

    def asignar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        if self.cursos:
            print(f"Cursos asignados para {self.nombre}:")
            for curso in self.cursos:
                print(f"- {curso.nombre} ({curso.catedratico})")
        else:
            print(f"{self.nombre} no tiene cursos asignados.")

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def eliminar_curso(self, nombre_curso):
        for curso in self.cursos:
            if curso.nombre == nombre_curso:
                self.cursos.remove(curso)
                print(f"El curso {nombre_curso} ha sido eliminado para {self.nombre}.")
                return
        print(f"{self.nombre} no está inscrito en el curso {nombre_curso}.")
