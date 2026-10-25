# EJERCICIO 4.2: SISTEMA DE ESTUDIANTES Y MATRICULAS

from abc import ABC, abstractmethod

class Estudiante(ABC):
    def __init__(self, nombre, codigo_estudiante, carrera, semestre_actual, pension_base=1000):
        # Atributos privados
        self.__nombre = nombre
        self.__codigo_estudiante = codigo_estudiante
        self.__carrera = carrera
        self.__semestre_actual = semestre_actual
        self._pension_base = pension_base
        
        # Atributo protegido
        self._cursos_matriculados = []

    def get_nombre(self):
        return self.__nombre

    def matricular_curso(self, curso):
        # Usamos el método para verificar créditos máximos de forma polimórfica
        if len(self._cursos_matriculados) < self.obtener_creditos_maximos():
            self._cursos_matriculados.append(curso)
            print(f"-> [MATRÍCULA ÉXITO] Estudiante {self.__nombre} matriculó el curso.")
        else:
            print(f"-> [ERROR] Límite de créditos/cursos alcanzado para {self.__nombre}.")

    # Métodos abstractos obligatorios (Contrato)
    @abstractmethod
    def calcular_pension(self):
        pass

    @abstractmethod
    def obtener_creditos_maximos(self):
        pass


# ==========================================
# HERENCIA, ENCAPSULAMIENTO Y POLIMORFISMO
# ==========================================

class EstudiantePregrado(Estudiante):
    def __init__(self, nombre, codigo_estudiante, carrera, semestre_actual, ano_ingreso, promedio_acumulado, beca_porcentaje, pension_base=1000):
        super().__init__(nombre, codigo_estudiante, carrera, semestre_actual, pension_base)
        self.ano_ingreso = ano_ingreso
        self.__promedio_acumulado = promedio_acumulado  # Atributo privado
        self.__beca_porcentaje = beca_porcentaje        # Atributo privado

    # Getter para el promedio (acceso controlado)
    def get_promedio(self):
        return self.__promedio_acumulado

    # Método privado para calcular el descuento de la beca
    def __calcular_descuento_beca(self):
        return self._pension_base * (self.__beca_porcentaje / 100)

    # Polimorfismo: Pensión restando la beca
    def calcular_pension(self):
        descuento = self.__calcular_descuento_beca()
        pension_final = self._pension_base - descuento
        return pension_final

    # Polimorfismo: Límite de créditos
    def obtener_creditos_maximos(self):
        return 22


class EstudiantePosgrado(Estudiante):
    def __init__(self, nombre, codigo_estudiante, carrera, semestre_actual, titulo_pregrado, tesis, pension_base=1800):
        super().__init__(nombre, codigo_estudiante, carrera, semestre_actual, pension_base)
        self.titulo_pregrado = titulo_pregrado
        self.tesis = tesis

    # Polimorfismo: Pensión de posgrado (tarifa alta)
    def calcular_pension(self):
        return self._pension_base

    # Polimorfismo: Límite de créditos
    def obtener_creditos_maximos(self):
        return 25


class EstudianteIntercambio(Estudiante):
    def __init__(self, nombre, codigo_estudiante, carrera, semestre_actual, universidad_origen, pais, duracion_estancia, pension_base=800):
        super().__init__(nombre, codigo_estudiante, carrera, semestre_actual, pension_base)
        self.universidad_origen = universidad_origen
        self.pais = pais
        self.duracion_estancia = duracion_estancia

    # Polimorfismo: Pensión con tarifa de convenio internacional
    def calcular_pension(self):
        return self._pension_base * 0.5  # 50% de descuento por convenio

    # Polimorfismo: Límite de créditos
    def obtener_creditos_maximos(self):
        return 18


class EducacionContinua(Estudiante):
    def __init__(self, nombre, codigo_estudiante, carrera, semestre_actual, empresa_patrocinadora, horario_especial, pension_base=600):
        super().__init__(nombre, codigo_estudiante, carrera, semestre_actual, pension_base)
        self.empresa_patrocinadora = empresa_patrocinadora
        self.horario_especial = horario_especial

    # Polimorfismo: Pensión modular por empresa
    def calcular_pension(self):
        return self._pension_base * 0.8  # Tarifa especial patrocinada

    # Polimorfismo: Límite de créditos
    def obtener_creditos_maximos(self):
        return 12


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("=== 1. CREANDO ESTUDIANTES DE CADA TIPO ===")
e1_pre = EstudiantePregrado("Ana Ruiz", "P101", "Ingeniería de Sistemas", 3, 2024, 4.5, 20)
e2_pre = EstudiantePregrado("Carlos Mesa", "P102", "Administración", 1, 2025, 3.8, 10)

e1_pos = EstudiantePosgrado("Lucía Gómez", "G201", "Maestría en IA", 1, "Ingeniera de Software", "En desarrollo")
e2_pos = EstudiantePosgrado("Mateo Botero", "G202", "Gerencia de Proyectos", 2, "Administrador", "Aprobada")

e1_int = EstudianteIntercambio("John Doe", "I301", "Ciencias de la Computación", 4, "MIT", "USA", "6 meses")
e2_int = EstudianteIntercambio("Marie Curie", "I302", "Física Aplicada", 3, "Sorbonne", "Francia", "1 año")

e1_con = EducacionContinua("Sofia Restrepo", "C401", "Python Avanzado", 1, "Globant", "Nocturno")
e2_con = EducacionContinua("Esteban Jaramillo", "C402", "Cloud Computing", 1, "MercadoLibre", "Fines de semana")

print("¡Estudiantes creados con éxito!\n")


print("=== 2. SIMULANDO MATRÍCULAS ===")
e1_pre.matricular_curso("Estructuras de Datos")
e1_pre.matricular_curso("Bases de Datos")
e1_pos.matricular_curso("Deep Learning Avanzado")
print()


print("=== 3. CALCULANDO PENSIONES (POLIMORFISMO) ===")
print(f"Pensión de {e1_pre.get_nombre()} (Pregrado con beca): ${e1_pre.calcular_pension()}")
print(f"Pensión de {e1_pos.get_nombre()} (Posgrado): ${e1_pos.calcular_pension()}")
print(f"Pensión de {e1_int.get_nombre()} (Intercambio con convenio): ${e1_int.calcular_pension()}")
print(f"Pensión de {e1_con.get_nombre()} (Educación Continua): ${e1_con.calcular_pension()}")