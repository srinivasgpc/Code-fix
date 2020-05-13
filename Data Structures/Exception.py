x =int(input('Enter the number: '))
def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')
    num_sqrt = x ** 0.5
    print('The square root of %0.3f is %0.3f'%(x ,num_sqrt))

sqrt(x)


