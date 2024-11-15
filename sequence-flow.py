# Problem: sequence and flow
a = int(input('a: '))
d = int(input('d: '))
n = int(input('n: '))
An = a + (n-1) * d
Sn = n / 2 * (2 * a + (n-1) * d)
print('An:', An, 'Sn:', int(Sn))