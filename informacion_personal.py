# Crear el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Sebastian",
    "edad": "23 años",
    "ciudad": "Tena",
    "profesion": "tecnologo"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Puyo"

# Agregar una nueva clave-valor que represente la profesión de la persona
informacion_personal["profesion"] = "tecnologo"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"  # Número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario actualizado
print(informacion_personal)