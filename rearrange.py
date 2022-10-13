#!/usr/bin/env python3

#importaciones
import re

#funciones
def rearrange_name(name):
	result = re.search(r"^([\w .]*), ([\w .]*)$", name)
	if result is None:
	    return name
	return f"{result[2]} {result[1]}"

#main program
if __name__ == "__main__":
    print(rearrange_name("Lovecraft, Alice") )
