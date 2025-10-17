A simple and interactive GUI calculator built using Python's Tkinter library. This calculator supports basic arithmetic operations, parentheses, percentages, and handles invalid inputs gracefully. The design features a modern dark theme with color-coded buttons for better usability.

Features
1.Basic Arithmetic Operations: Addition (+), Subtraction (-), Multiplication (*), Division (/)
2.Parentheses: Automatically inserts opening or closing parentheses depending on the context
3.Percentage Calculation: Converts any valid input into its percentage equivalent
4.Decimal Support: Handles floating point numbers
5.Error Handling:
Displays "Can't divide by zero" for division by zero
Displays "Invalid" for invalid mathematical expressions
Responsive Design: Buttons are clearly separated and color-coded for operators, numbers, and special functions
Dark Theme UI: Sleek, modern design with white numbers and orange/green function keys

How It Works
The calculator uses a Tkinter Entry widget to display the current input and results.
Each button is linked to a function:
press(number): Adds a digit to the input
operators(symbol): Adds an operator to the input
parenthesis(): Inserts an opening or closing parenthesis based on the context
percent(): Converts the current input into a percentage
submit(): Evaluates the expression and displays the result
clear(): Clears the input
Expression Handling:
Replaces custom symbols like × and ÷ with Python-friendly * and /
Supports implicit multiplication (e.g., 2(3+4) is interpreted as 2*(3+4))
Removes leading zeros for correct evaluation

Technologies Used
Python 3.x
Tkinter (Standard Python GUI library)
Regular Expressions (Regex) for parsing input expressions
