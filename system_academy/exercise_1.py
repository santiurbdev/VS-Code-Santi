# EJERCICIO 4.1: GESTION DE CURSOS ACADEMICOS

from abc import ABC, abstractmethod

class CursoAcademico(ABC):
    def __init__(self, codigo_curso, nombre, creditos, semestre, limite_estudiantes=30):
        self.__codigo_curso = codigo_curso
        self.__nombre = nombre
        self.__creditos = creditos
        self.__semestre = semestre
        self.__limite_estudiantes = limite_estudiantes
        self._estudiantes_inscritos = []

    def get_nombre(self):
        return self.__nombre

    def __validar_prerrequisitos(self, estudiante):
        return True

    def inscribir_estudiante(self, estudiante):
        if len(self._estudiantes_inscritos) < self.__limite_estudiantes:
            if self.__validar_prerrequisitos(estudiante):
                self._estudiantes_inscritos.append(estudiante)
                print(f"-> [EXITO] Estudiante {estudiante} inscrito en {self.__nombre}.")
            else:
                print(f"-> [DENEGADO] Estudiante {estudiante} no cumple con los prerequisitos.") 
        else:
            print(f"-> [ERROR] Curso {self.__nombre} lleno.") 

    @abstractmethod
    def calcular_nota_final(self, estudiante):
        pass

    @abstractmethod
    def obtener_requesitos(self):
        pass

#-----------------------------------------------------------------------------------------------------------------

class CursoTeorico(CursoAcademico):
    def __init__(self, codigo_curso, nombre, creditos, semestre, horas_clase, num_examenes):
        super().__init__(codigo_curso, nombre, creditos, semestre)
        self.__horas_clase = horas_clase
        self.__num_examenes = num_examenes

    def calcular_nota_final(self, nota_examenes, nota_tareas):  # Regla del Teórico (60% exámenes + 40% tareas)
        nota_final = (nota_examenes * 0.6) + (nota_tareas * 0.4)
        return nota_final

    def obtener_requesitos(self):
        return "Prerrequisito: Lectura previa de bibliografía y seminario básico."


class CursoPractico(CursoAcademico):
    def __init__(self, codigo_curso, nombre, creditos, semestre, horas_practicas, proyectos):  
        super().__init__(codigo_curso, nombre, creditos, semestre)
        self.__horas_practicas = horas_practicas
        self.__proyectos = proyectos

    def calcular_nota_final(self, nota_proyectos, nota_teoria):  # Regla del Práctico (70% proyectos + 30% teoría)
        nota_final = (nota_proyectos * 0.7) + (nota_teoria * 0.3)
        return nota_final

    def obtener_requesitos(self):
        return "Prerrequisito: Haber aprobado el curso teórico correspondiente."


class CursoLaboratorio(CursoAcademico):
    def __init__(self, codigo_curso, nombre, creditos, semestre, laboratorio_asignado, equipos):
        super().__init__(codigo_curso, nombre, creditos, semestre)
        self.__laboratorio_asignado = laboratorio_asignado
        self.__equipos = equipos

    def calcular_nota_final(self, nota_practicas, nota_informe):  # Regla del Laboratorio (80% prácticas + 20% informe)
        nota_final = (nota_practicas * 0.8) + (nota_informe * 0.2)
        return nota_final

    def obtener_requesitos(self):
        return "Prerrequisito: Inducción de seguridad y manejo de equipos aprobada."


class Seminario(CursoAcademico):
    def __init__(self, codigo_curso, nombre, creditos, semestre, num_exposiciones, investigacion_requerida):
        super().__init__(codigo_curso, nombre, creditos, semestre)
        self.__num_exposiciones = num_exposiciones
        self.__investigacion_requerida = investigacion_requerida

    def calcular_nota_final(self, nota_exposicion, nota_investigacion, nota_participacion):  # Regla del Seminario (50% presentaciones + 50% participación)
        nota_final = (nota_exposicion * 0.5) + (nota_investigacion * 0.3) + (nota_participacion * 0.2)
        return nota_final

    def obtener_requesitos(self):
        return "Prerrequisito: Estar cursando últimos semestres de la carrera."


#-----------------------------------------------------------------------------------------------------------------  

print("=== 1. CURSOS DE CADA TIPO ===")

curso1_teorico = CursoTeorico("T101", "Matematicas Discretas", 3, 2, 48, 2)
curso2_teorico = CursoTeorico("T102", "Estructuras de Datos", 4, 3, 64, 3)

curso1_practico = CursoPractico("P201", "Laboratorio de Programación", 2, 2, 32, 2)
curso2_practico = CursoPractico("P202", "Desarrollo Web", 3, 3, 48, 2)

curso1_lab = CursoLaboratorio("L301", "Lab de Redes", 2, 4, "Lab 3", ["Routers", "Switches"])
curso2_lab = CursoLaboratorio("L302", "Lab de Base de Datos", 2, 3, "Lab 1", ["Servidores SQL"])

curso1_sem = Seminario("S401", "Ética Profesional", 2, 5, 2, "Ensayo final")
curso2_sem = Seminario("S402", "Innovación Tecnológica", 2, 6, 1, "Proyecto de investigación")

print("¡Cursos creados con éxito!\n")


print("=== 2. INSCRIBIENDO ESTUDIANTES ===")
curso1_practico.inscribir_estudiante("Juliana Gomez")
curso1_practico.inscribir_estudiante("Carlos Pérez")
curso1_teorico.inscribir_estudiante("Juan Uribe")
print()


print("=== 3. PROBANDO EL POLIMORFISMO (Cálculo de Notas) ===")
# Aunque cada uno usa una fórmula distinta, todos usan el método calcular_nota_final
nota_teo = curso1_teorico.calcular_nota_final(4.5, 4.0)
print(f"Nota final en curso teórico ({curso1_teorico.get_nombre()}): {nota_teo}")

nota_prac = curso1_practico.calcular_nota_final(4.8, 3.5)
print(f"Nota final en curso práctico ({curso1_practico.get_nombre()}): {nota_prac}")

nota_lab = curso1_lab.calcular_nota_final(5.0, 4.2)
print(f"Nota final en laboratorio ({curso1_lab.get_nombre()}): {nota_lab}")

nota_sem = curso1_sem.calcular_nota_final(4.0, 4.5, 5.0)
print(f"Nota final en seminario ({curso1_sem.get_nombre()}): {nota_sem}")