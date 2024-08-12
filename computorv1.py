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
	for exp in sorted(left_terms, reverse=True):
		coef = left_terms[exp]
		term = f"{int(absolute(coef))} * X^{exp}" if coef.is_integer() else f"{absolute(coef)} * X^{exp}"
		if coef < 0:
			term = f"- {term}"
		elif reduced:
			term = f"+ {term}"
		reduced.append(term)

	reduced_result = ' '.join(reduced)
	return f"{reduced_result} = 0"

def square_root(num):
	"""
		Returns the square root of a given number.

		Args:
			num (float): The number to find the square root of.

		Returns:
			num (float): The square root of num.
	"""
	return num ** 0.5

def solve_polynomial(equation, degree):
	terms = extract_terms(equation.split('=')[0])

	if degree == 0:
		result = sum(terms.values())
		if result == 0:
			print('Any real number is a solution.')
		else:
			print('There is no solution.')
	elif degree == 1:
		const_term = 0
		coef = 0
		for exp in terms:
			if exp == 0:
				const_term += terms[exp]
			else:
				coef = terms[exp]
			
		if coef == 0:
			if const_term == 0:
				print('Any real number is a solution.')
			else:
				print('There is no solution.')
		else:
			result = -const_term / coef
			print(f'The solution is:\n{result}')
	elif degree == 2:
		delta = (terms[1] ** 2) - (4 * terms[2] * terms[0])
		if delta < 0:
			print('Discriminant is strictly negative, there is two complex solutions:')
			print(f'α + β * i = (-2b + i√|Δ|) / 2a = ({-terms[1]} + i√|{delta}|) / 2 * {terms[2]}')
			print(f'α - β * i = (-2b - i√|Δ|) / 2a = ({-terms[1]} - i√|{delta}|) / 2 * {terms[2]}')
		elif delta == 0:
			result = -terms[1] / (2 * terms[2])
			print(f'Discriminant is equal to zero, there is exactly one real solution:\n{result}')
		else:
			result_1 = (-terms[1] - square_root(delta)) / (2 * terms[2])
			result_2 = (-terms[1] + square_root(delta)) / (2 * terms[2])
			print(f'Discriminant is strictly positive, the two solutions are:\n{round(result_1, 6)}\n{round(result_2, 6)}')
