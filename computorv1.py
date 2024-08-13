import re
import sys
from utils import *

def is_valid_expression(expression):
	"""
		Parse the polynomial expression

		Args:
			expression (str): Polynomial expression

		Returns:
			bool: if the Polynomial expression is valid returns True, else returns False
	"""
	if not expression.strip():
		return False
	elif '=' not in expression:
		return False
	return True

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
		if term:
			if 'X' in term:
				if '*' not in term:
					term = '1*' + term
				if '^' not in term:
					term += '^1'
			elif is_integer(term) or is_float(term):
				term += '*X^0'
			else:
				sys.exit("Error: enter a valid Polynomial equation!")

			coef, exp = term.split('*X^')
			coef = float(coef)
			exp = int(exp)

			if exp in terms:
				terms[exp] += coef
			else:
				if coef != 0:
					terms[exp] = coef
	return terms

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
		coef_str = int(absolute(coef)) if coef.is_integer() else absolute(coef)

		if coef not in {1, -1}:
			if exp not in {1, 0}:
				term = f"{coef_str} * X^{exp}"
			elif exp == 0:
				term = f"{coef_str}"
			else:
				term = f"{coef_str} * X"
		elif coef in {1, -1}:
			if exp not in {1, 0}:
				term = f"X^{exp}"
			elif exp == 0:
				term = "1"
			else:
				term = "X"

		if coef < 0:
			term = f"- {term}"
		elif reduced:
			term = f"+ {term}"
		reduced.append(term)

	reduced_result = ' '.join(reduced)
	return f"{reduced_result} = 0"

def solve_polynomial(equation):
	"""
		Solve a polynomial equation od degree 2 or below

		Args:
			equation (str): the polynomial equation to solve
	"""
	terms = extract_terms(equation.split('=')[0])

	polynomial_degree = max_key(terms.keys()) if terms.keys() else 0
	print(f'Polynomial degree: {polynomial_degree}')
	
	if polynomial_degree > 2:
		sys.exit('The polynomial degree is strictly greater than 2, I can\'t solve.')

	if polynomial_degree == 0:
		result = sum(terms.values())
		if result == 0:
			print('Any real number is a solution.')
		else:
			print('There is no solution.')
	elif polynomial_degree == 1:
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
	elif polynomial_degree == 2:
		delta = (terms[1] ** 2) - (4 * terms[2] * (terms[0] if 0 in terms else 0))
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
