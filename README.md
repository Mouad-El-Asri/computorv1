# ComputorV1

ComputorV1 is a Python program to parse, reduce, and solve polynomial equations of degree up to 2.

## 📦 Features

- **Polynomial Equation Parsing**: Validates and parses polynomial equations from user input in the format `a ∗ x^p`.
- **Polynomial Equation Reduction**: Reduces equations to their canonical form.
- **Polynomial Degree Detection**: Identifies the highest power of `x` in the reduced form.
- **Polynomial Equation Solving**: Finds solutions for equations of degree 0, 1, or 2, including real and complex solutions.
- **Polynomial Discriminant Calculation**: For quadratic equations, computes: Δ = b² - 4ac
	- **Solution Computation**:
	  - Δ > 0 → Two distinct real solutions.
	  - Δ = 0 → One real solution.
	  - Δ < 0 → No real solution (optional handling of complex numbers).

## 🛠️ Usage

1. Start the program by running:
  	```zsh
  	python3 run.py
  	```

2. When prompted, type a polynomial equation in the format:
  	```
  	<number> * X^<degree> [+/- ...] = <number> * X^<degree> [+/- ...]
  	```
	
  	Example:

  	```
  	5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
  	```

3. The program will:
  - Check if the input is valid
  - Convert the equation to its reduced form
  - Show the polynomial degree
  - Calculate and display the solution(s) if the degree is 0, 1, or 2
  - If the degree is greater than 2, print a message that it cannot solve the equation
  - If something is wrong, the program will handle the error and print an error message.

## 🧮 Example

### Example I
```
Enter the polynomial equation: "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131
```
### Example II
```
Enter the polynomial equation: "5 * X^0 + 4 * X^1 = 4 * X^0"
Reduced form: 1 * X^0 + 4 * X^1 = 0
Polynomial degree: 1
The solution is:
-0.25
```
### Example III
```
Enter the polynomial equation: "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
Polynomial degree: 3
The polynomial degree is strictly greater than 2, I can't solve.
```

## 📁 Project Structure

```
computorv1/
├── run.py                  # Main entry point, handles user interaction
├── computorv1.py           # Core logic for parsing, reducing, and solving equations
├── utils.py                # Utility functions for type checking, math operations, etc.
├── LICENSE                 # MIT License
├── en.subject_computerv1.pdf # Subject description
└── README.md               # Project documentation
```

## ⚙️ Requirements

-   Python 3.10+

## 📚 Resources

-   [Computorv1 Subject File](./en.subject_computerv1.pdf)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project is part of the **1337 Coding School (42 Network)** curriculum.
