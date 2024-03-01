def mult(*args):
    total = 1
    for num in args:
        total *= num
    return total
# def impar_ou_par():
    # if 
m = mult(10, 2, 3, 4, 5)
print(m)

def par_ou_impar(num):
    resto = num % 2       
    print(resto)
    if resto == 0:
        return 'par'
    return 'impar'
    
i = par_ou_impar(30)

print(i)