def soma(x, y, z=None):
    if z is not None:
        print(f'{x=}, {y=}, {z=}', x+y+y)
    else:
        print(f'{x=}, {y=}', x+y)

        

soma(1, 2)
soma(4,5,8)
soma(z=10, y=25, x=50)