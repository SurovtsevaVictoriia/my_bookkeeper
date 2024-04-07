s = '12.25.24'
a = ['a', 'b', 'c']
try:
    b = 'a'
    if b not in a:
        raise ValueError
except ValueError:
    print('exception caught')
else: 
    print('no expcep')