# EJERCICIO 4.4: SISTEMA DE DOCENTES Y ASIGNACIONES

from abc import ABC, abstractmethod

class Docente(ABC):
    def __init__(self, nombre, codigo_docente, especialidad, anos_experiencia, salario_base=3000):
        # Atributos privados
        self.__nombre = nombre
        self.__codigo_docente = codigo_docente
        self.__especialidad = especialidad
        self._anos_experiencia = anos_experiencia  # Cambiado a protegido para las clases hijas
        self._salario_base = salario_base
        
        # Atributo protegido: Lista de cursos asignados
        self._cursos_asignados = []

    def get_nombre(self):
        return self.__nombre

    # Método concreto para asignar cursos validando la carga máxima de forma polimórfica
    def asignar_curso(self, curso):
        if len(self._cursos_asignados) < self.obtener_carga_maxima():
            self._cursos_asignados.append(curso)
            print(f"-> [ASIGNACIÓN ÉXITO] Curso '{curso}' asignado al docente {self.__nombre}.")
        else:
            print(f"-> [ERROR] El docente {self.__nombre} ha alcanzado su carga máxima de cursos.")

    # Métodos abstractos obligatorios (Contrato)
    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def obtener_carga_maxima(self):
        pass


# ==========================================
#  HERENCIA, ENCAPSULAMIENTO Y POLIMORFISMO
# ==========================================

class DocenteTiempoCompleto(Docente):
    def __init__(self, nombre, codigo_docente, especialidad, anos_experiencia, dedicacion_exclusiva=True, investigacion=True, salario_base=4000):
        super().__init__(nombre, codigo_docente, especialidad, anos_experiencia, salario_base)
        self.dedicacion_exclusiva = dedicacion_exclusiva
        self.investigacion = investigacion

    # Método privado para calcular bonificaciones según los años de experiencia
    def __calcular_bonificaciones(self):
        return self._anos_experiencia * 150  # 150 por cada año de experiencia

    # Polimorfismo: Salario base + bonificaciones privadas
    def calcular_salario(self):
        bono = self.__calcular_bonificaciones()
        return self._salario_base + bono

    # Polimorfismo: Carga máxima de cursos
    def obtener_carga_maxima(self):
        return 4


class DocenteTiempoParcial(Docente):
    def __init__(self, nombre, codigo_docente, especialidad, anos_experiencia, horas_semana, tarifa_por_hora):
        super().__init__(nombre, codigo_docente, especialidad, anos_experiencia)
        self.__horas_semana = horas_semana          # Atributo privado
        self.__tarifa_por_hora = tarifa_por_hora    # Atributo privado

    def get_horas_semana(self):
        return self.__horas_semana

    # Polimorfismo: Salario calculado por horas trabajadas al mes (4 semanas)
    def calcular_salario(self):
        return self.__horas_semana * self.__tarifa_por_hora * 4

    # Polimorfismo: Carga máxima de cursos
    def obtener_carga_maxima(self):
        return 2


class DocenteInvitado(Docente):
    def __init__(self, nombre, codigo_docente, especialidad, anos_experiencia, institucion_origen, periodo_estancia, honorarios):
        super().__init__(nombre, codigo_docente, especialidad, anos_experiencia)
        self.institucion_origen = institucion_origen
        self.periodo_estancia = periodo_estancia
        self.__honorarios = honorarios  # Atributo privado

    # Polimorfismo: Salario basado en honorarios fijos por estancia
    def calcular_salario(self):
        return self.__honorarios

    # Polimorfismo: Carga máxima de cursos
    def obtener_carga_maxima(self):
        return 1


class Asistente(Docente):
    def __init__(self, nombre, codigo_docente, especialidad, anos_experiencia, estudios_posgrado, docente_supervisor, es_practicante):
        super().__init__(nombre, codigo_docente, especialidad, anos_experiencia, salario_base=1500)
        self.estudios_posgrado = estudios_posgrado
        self.docente_supervisor = docente_supervisor
        self.es_practicante = es_practicante

    # Polimorfismo: Salario base de asistente
    def calcular_salario(self):
        return self._salario_base

    # Polimorfismo: Carga máxima de cursos
    def obtener_carga_maxima(self):
        return 1


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

print("=== 1. CREANDO DOCENTES DE CADA TIPO ===")
d1_tc = DocenteTiempoCompleto("Dr. Roberto Gómez", "TC01", "Arquitectura de Software", 10)
d2_tc = DocenteTiempoCompleto("Dra. Marcela Ríos", "TC02", "Inteligencia Artificial", 6)

d1_tp = DocenteTiempoParcial("Ing. Andrés Castro", "TP01", "Bases de Datos", 4, 12, 50)
d2_tp = DocenteTiempoParcial("Esp. Diana Marín", "TP02", "Seguridad Informática", 5, 10, 60)

d1_inv = DocenteInvitado("Dr. Alan Turing Jr.", "INV01", "Computación Cuántica", 15, "Oxford", "3 meses", 5000)
d2_inv = DocenteInvitado("Dra. Ada Lovelace", "INV02", "Algoritmos Avanzados", 12, "MIT", "6 meses", 7000)

d1_asist = Asistente("Juan Esteban", "AS01", "Desarrollo Web", 1, False, "Dr. Roberto Gómez", True)
d2_asist = Asistente("Valeria Botero", "AS02", "Redes", 2, True, "Dra. Marcela Ríos", False)

print("¡Docentes creados con éxito!\n")


print("=== 2. ASIGNANDO CURSOS (Respetando Carga Máxima) ===")
d1_tc.asignar_curso("Ingeniería de Software I")
d1_tc.asignar_curso("Arquitectura Limpia")
d1_tc.asignar_curso("Patrones de Diseño")

d1_tp.asignar_curso("Fundamentos de Bases de Datos")
d1_tp.asignar_curso("SQL Avanzado")
d1_tp.asignar_curso("Optimización de Consultas")  
print()


print("=== 3. CALCULANDO PLANILLA DOCENTE (POLIMORFISMO) ===")
print(f"Salario de {d1_tc.get_nombre()} (Tiempo Completo): ${d1_tc.calcular_salario()}")
print(f"Salario de {d1_tp.get_nombre()} (Tiempo Parcial): ${d1_tp.calcular_salario()}")
print(f"Salario de {d1_inv.get_nombre()} (Invitado): ${d1_inv.calcular_salario()}")
print(f"Salario de {d1_asist.get_nombre()} (Asistente): ${d1_asist.calcular_salario()}")