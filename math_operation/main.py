from math_operation import addition,division,multiplication,subtraction

x = int(input("number 1: "))
y = int(input("number 2: "))

result_addition = addition.add_number(x, y)
result_subtraction = subtraction.sub_number(x, y)
result_multiplication = multiplication.multi_number(x, y)
result_division = division.div_number(x, y)

print(f" {x} + {y} = {result_addition}")
print(f" {x} - {y} = {result_subtraction}")
print(f" {x} * {y} = {result_multiplication}")
print(f" {x} / {y} = {result_division}")