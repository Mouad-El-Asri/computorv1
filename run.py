from computorv1 import *

def main():
	polynomial__equation = input('Enter the polynomial equation: ')
	if not is_valid_expression(polynomial__equation):
		sys.exit('Error: enter a valid Polynomial equation!')

	equation_reduced_form = reduced_form(polynomial__equation)
	print(f'Reduced form: {equation_reduced_form}')

	solve_polynomial(equation_reduced_form)

if __name__ == '__main__':
	main()
