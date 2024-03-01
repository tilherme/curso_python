name = input('Digite seu nome: ')
index = 0
new_name = ''
while index < len(name):
    # print(name[index])
    l =name[index] + '!'
    new_name += l

    index += 1
print(new_name)
 
    # break