def is_integer(string):
	"""
		Checks if the given string can be converted to an integer.

		Args:
			string (str): The string to be checked for integer conversion.

		Returns:
			bool: `True` if the string can be converted to an integer, `False` otherwise.
	"""
	try:
		int(string)
		return True
	except ValueError:
		return False

def is_float(string):
	"""
		Checks if the given string can be converted to a float.

		Args:
			string (str): The string to be checked for float conversion.

		Returns:
			bool: `True` if the string can be converted to a float, `False` otherwise.
	"""
	try:
		float(string)
		return True
	except ValueError:
		return False

def absolute(num):
	"""
		Returns the absolute value of a number.

		Args:
			num (float): The number for which to find the absolute value.

		Returns:
			(float): The absolute value of the input number.
	"""
	abs_num = num if num >= 0 else -num
	return abs_num

def square_root(num):
	"""
		Returns the square root of a given number.

		Args:
			num (float): The number to find the square root of.

		Returns:
			num (float): The square root of num.
	"""
	return num ** 0.5
