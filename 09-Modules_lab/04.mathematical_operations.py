from modules import calculation

# first_number = float(input("Enter the first float number: "))
# second_number = int(input("Enter the second number: "))
# operation = input("Enter the operation (+,-,/,*,^): ")
string = input("Enter the expression for calculation: ")
first_number, operation, second_number = string.split()

print(f'{calculation(float(first_number), operation, int(second_number)):.2f}')
