# Problem: Reverse String
# Way: 1
def reverse_string (text):
    string = text[::-1]
    return string

# Way: 2
def reverse (text):
    reversed_string = ''
    for char in text:
        reversed_string = char + reversed_string
    return reversed_string

get_input = input('Your Text: ')
print('Using First Way:', reverse_string(get_input))
print('Using Second Way:', reverse(get_input))