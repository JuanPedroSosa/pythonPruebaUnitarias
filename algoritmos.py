"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120
"""

def fibonacci(number):
	if number == 0: return 0
	elif number == 1: return 1
	else: return fibonacci(number -1) + fibonacci(number -2)

def palindromo(setence):
	""" Retorna verdadero si es un palíndromo
	en caso contrario retorna falso
	setence string o entero
	>>> palindromo("anita lava la tina")
	True
	>>> palindromo(12321)
	True
	"""
	setence = str(setence).lower().replace(" ", "")
	return setence == setence[::-1]


class Recursivo:
	def factorial(self, number):
		if number == 0: return 1
		else: return number * self.factorial(number -1)


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	doctest.testfile("test.txt")
