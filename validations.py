#!/usr/bin/env python3
#aquí en semana 5 aprendemos a crear nuestros propios errores
#assertions desapareceran del script tras produccion pero raise se mantendrán, ese es el criterio de diferencia
def validate_user(username, minlen):
    assert type(username) == str, "username must be a string" #verifica que el tipo es el mismo
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum(): # The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers)
        return False
    return True
