from computorv1 import *

def main():
	polynomial__equation = input('Enter the polynomial equation: ')

	equation_reduced_form = reduced_form(polynomial__equation)
	print(f'Reduced form: {equation_reduced_form}')

	polynomial_deg = polynomial_degree(equation_reduced_form)
	print(f'Polynomial degree: {polynomial_deg}')
	
	if polynomial_deg > 2:
		print('The polynomial degree is strictly greater than 2, I can\'t solve.')
	else:
		solve_polynomial(equation_reduced_form, polynomial_deg)

if __name__ == '__main__':
	main()
