def polynomial_degree(equation):
	"""
		Determines the degree of a polynomial equation.

		Args:
			equation (str): Polynomial equation

		Returns:
			int: The highest exponent (degree) in the polynomial.
	"""
	equation = equation.split('=')[0].strip()

	max_degree = 0
	index = 0
	while True:
		index = equation.find('X^', index)
		if index == -1:
			break

		start = index + 2
		end = start
		while end < len(equation) and equation[end].isdigit():
			end += 1


		exponent = int(equation[start:end])
		if exponent > max_degree:
			max_degree = exponent
		
		index = end
	
	return max_degree

def extract_terms(expression):
	"""
		Parses a polynomial expression and returns a dictionary of terms.

		Args:
			expression (str): Polynomial expression with terms.
		
		Returns:
        	dict: Dictionary where keys are exponents and values are aggregated coefficients.
	"""
	expression = expression.replace(' ', '')
	terms = {}
	for term in expression.replace('-', '+-').split('+'):
		if '*X^' in term:
			coef, exp = term.split('*X^')
			coef = float(coef)
			exp = int(exp)

			if exp in terms:
				terms[exp] += coef
			else:
				terms[exp] = coef
	
	return terms

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

def reduced_form(equation):
	"""
		Reduces a polynomial equation to its reduced form.

		Args:
			equation (str): Polynomial equation

		Returns:
        	str: The reduced polynomial equation with terms combined.
	"""

	left_side, right_side = equation.split('=')[:2]
	left_side = left_side.strip()
	right_side = right_side.strip()

	left_terms = extract_terms(left_side)
	right_terms = extract_terms(right_side)

	for exp in right_terms:
		if exp in left_terms:
			left_terms[exp] -= right_terms[exp]
		else:
			left_terms[exp] = -right_terms[exp]

	reduced = []
	for exp in sorted(left_terms, reverse=False):
		coef = left_terms[exp]
		term = f"{int(absolute(coef))} * X^{exp}" if coef.is_integer() else f"{absolute(coef)} * X^{exp}"
		if coef < 0:
			term = f"- {term}"
		elif reduced:
			term = f"+ {term}"
		reduced.append(term)

	reduced_result = ' '.join(reduced)
	return f"{reduced_result} = 0"