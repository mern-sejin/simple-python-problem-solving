# PROBLEM-3: sum of the numbers
def calculate (num, limit, add):
    number = num 
    sum = 0
    while number <= limit:
        sum += number
        number += add
    return sum

num_input = int(input('Number: '))
limit_input = int(input('Limit: '))
add_input = int(input('Add: '))

result = calculate(num_input, limit_input, add_input)
print(result)