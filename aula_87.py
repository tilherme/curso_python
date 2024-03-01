def test(*args):
    total = 0
    for num in args:
        total += num
    return total

soma_1_2_3 = test(1,2,3)
print(soma_1_2_3)
soma_4_5_6 = test(4,5,6)
print(soma_4_5_6)
numeros = 1,2,3,4,5,6,7,8,9,10
outra_soma = test(*numeros)
print(sum(numeros))
print(outra_soma)