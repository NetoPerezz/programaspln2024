# Definir la lista de días de la semana laboral
semana_laboral = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Imprimir la semana laboral
print("Semana laboral:", semana_laboral)

# Imprimir el primer día de la semana
print("Día 1:", semana_laboral[0])

# Cambiar el quinto día a "Sábado"
semana_laboral[4] = "Sábado"

# Imprimir la semana laboral actualizada
print("Semana laboral:", semana_laboral)

# Cambiar el quinto día de vuelta a "Viernes"
semana_laboral[4] = "Viernes"

# Obtener la longitud de la lista
longitud_lista = len(semana_laboral)
print("Longitud:", longitud_lista)

# Encontrar el índice de "Miércoles"
posicion = semana_laboral.index("Miércoles")
print("Posición de Miércoles:", posicion)

# Agregar "Sábado" al final de la lista
semana_laboral.append("Sábado")

# Imprimir la semana laboral final
print("Semana laboral:", semana_laboral)
