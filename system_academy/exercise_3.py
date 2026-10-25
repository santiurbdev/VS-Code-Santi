# EJERCICIO 4.3: SISTEMA DE EVALUACIONES Y CALIFICACIONES

from abc import ABC, abstractmethod

class Evaluacion(ABC):
    def __init__(self, codigo_eval, curso, fecha, peso_porcentaje):
        # Atributos privados
        self.__codigo_eval = codigo_eval
        self.__curso = curso
        self.__fecha = fecha
        self.__peso_porcentaje = peso_porcentaje
        
        # Atributo protegido: Diccionario para guardar estudiantes y sus notas
        self._calificaciones = {}

    def get_codigo(self):
        return self.__codigo_eval

    # Método concreto para registrar notas validando que estén en el rango correcto (0 a 5 o 0 a 20 según escala, usaremos 0 a 5 común en Colombia, o 0 a 20 como pide el enunciado)
    def registrar_calificacion(self, estudiante, nota):
        if 0 <= nota <= 20: # El enunciado pide validación de 0-20
            self._calificaciones[estudiante] = nota
            print(f"-> [REGISTRO] Nota {nota} asignada a {estudiante} en {self.__curso}.")
        else:
            print(f"-> [ERROR] Nota inválida para {estudiante}. Debe estar entre 0 y 20.")

    # Métodos abstractos obligatorios (Contrato)
    @abstractmethod
    def calcular_nota_estudiante(self, estudiante):
        pass

    @abstractmethod
    def generar_estadisticas(self):
        pass


# ==========================================
# HERENCIA, ENCAPSULAMIENTO Y POLIMORFISMO
# ==========================================

class ExamenEscrito(Evaluacion):
    def __init__(self, codigo_eval, curso, fecha, peso_porcentaje, num_preguntas, tiempo_minutos, tipo):
        super().__init__(codigo_eval, curso, fecha, peso_porcentaje)
        self.num_preguntas = num_preguntas
        self.tiempo_minutos = tiempo_minutos
        self.tipo = tipo  # multiple, desarrollo

    # Método privado para aplicar una curva de puntos extra a la nota
    def __aplicar_curva(self, nota):
        nota_con_curva = min(20.0, nota + 1.0)  # Sube 1 punto extra sin pasar de 20
        return nota_con_curva

    # Polimorfismo: Calcula la nota aplicando la curva privada
    def calcular_nota_estudiante(self, estudiante):
        if estudiante in self._calificaciones:
            nota_original = self._calificaciones[estudiante]
            return self.__aplicar_curva(nota_original)
        return "Estudiante sin calificar"

    # Polimorfismo: Generar estadísticas del examen
    def generar_estadisticas(self):
        if not self._calificaciones:
            return "No hay calificaciones registradas."
        
        notas = [self.__aplicar_curva(n) for n in self._calificaciones.values()]
        promedio = sum(notas) / len(notas)
        aprobados = sum(1 for n in notas if n >= 11)  # Asumiendo 11 para aprobar en escala de 0-20
        desaprobados = len(notas) - aprobados
        
        return f"[Estadísticas Examen] Promedio: {promedio:.2f} | Aprobados: {aprobados} | Desaprobados: {desaprobados}"


class PracticaCalificada(Evaluacion):
    def __init__(self, codigo_eval, curso, fecha, peso_porcentaje, ejercicios, tiempo_minutos, puede_consultar_material):
        super().__init__(codigo_eval, curso, fecha, peso_porcentaje)
        self.ejercicios = ejercicios
        self.tiempo_minutos = tiempo_minutos
        self.puede_consultar_material = puede_consultar_material

    def calcular_nota_estudiante(self, estudiante):
        return self._calificaciones.get(estudiante, "Estudiante sin calificar")

    def generar_estadisticas(self):
        if not self._calificaciones:
            return "No hay calificaciones registradas."
        
        notas = list(self._calificaciones.values())
        promedio = sum(notas) / len(notas)
        aprobados = sum(1 for n in notas if n >= 11)
        desaprobados = len(notas) - aprobados
        
        return f"[Estadísticas Práctica] Promedio: {promedio:.2f} | Aprobados: {aprobados} | Desaprobados: {desaprobados}"


class ProyectoGrupal(Evaluacion):
    def __init__(self, codigo_eval, curso, fecha, peso_porcentaje, num_integrantes, etapas, peso_por_etapa):
        super().__init__(codigo_eval, curso, fecha, peso_porcentaje)
        self.num_integrantes = num_integrantes
        self.etapas = etapas
        self.peso_por_etapa = peso_por_etapa

    def calcular_nota_estudiante(self, estudiante):
        return self._calificaciones.get(estudiante, "Estudiante sin calificar")

    def generar_estadisticas(self):
        if not self._calificaciones:
            return "No hay calificaciones registradas."
        
        notas = list(self._calificaciones.values())
        promedio = sum(notas) / len(notas)
        aprobados = sum(1 for n in notas if n >= 11)
        desaprobados = len(notas) - aprobados
        
        return f"[Estadísticas Proyecto] Promedio: {promedio:.2f} | Aprobados: {aprobados} | Desaprobados: {desaprobados}"


class Exposicion(Evaluacion):
    def __init__(self, codigo_eval, curso, fecha, peso_porcentaje, duracion_minutos, rubrica_evaluacion, preguntas_respuestas):
        super().__init__(codigo_eval, curso, fecha, peso_porcentaje)
        self.duracion_minutos = duracion_minutos
        self.rubrica_evaluacion = rubrica_evaluacion
        self.preguntas_respuestas = preguntas_respuestas

    def calcular_nota_estudiante(self, estudiante):
        return self._calificaciones.get(estudiante, "Estudiante sin calificar")

    def generar_estadisticas(self):
        if not self._calificaciones:
            return "No hay calificaciones registradas."
        
        notas = list(self._calificaciones.values())
        promedio = sum(notas) / len(notas)
        aprobados = sum(1 for n in notas if n >= 11)
        desaprobados = len(notas) - aprobados
        
        return f"[Estadísticas Exposición] Promedio: {promedio:.2f} | Aprobados: {aprobados} | Desaprobados: {desaprobados}"


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("=== 1. CREANDO EVALUACIONES DE CADA TIPO ===")
ex_escrito = ExamenEscrito("EX101", "Matemáticas Discretas", "2026-10-15", 30, 10, 90, "Desarrollo")
pr_cal = PracticaCalificada("PR201", "Programación I", "2026-10-18", 20, 5, 120, True)
pro_grupal = ProyectoGrupal("PJ301", "Bases de Datos", "2026-10-25", 40, 3, 4, "25% c/u")
expo = Exposicion("EP401", "Ingeniería de Software", "2026-10-28", 10, 15, "Estándar", True)

print("¡Evaluaciones creadas con éxito!\n")


print("=== 2. INGRESANDO CALIFICACIONES ===")
ex_escrito.registrar_calificacion("Ana Ruiz", 14.0)
ex_escrito.registrar_calificacion("Carlos Mesa", 9.5)
ex_escrito.registrar_calificacion("Lucía Gómez", 18.0)

pr_cal.registrar_calificacion("Ana Ruiz", 16.0)
pr_cal.registrar_calificacion("Carlos Mesa", 10.0)
print()


print("=== 3. GENERANDO ESTADÍSTICAS (POLIMORFISMO) ===")
print(ex_escrito.generar_estadisticas())
print(pr_cal.generar_estadisticas())