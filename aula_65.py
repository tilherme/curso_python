for i in range(1, 10):
    if i == 2:
        print('i é 2')
        continue

    if i == 5:
        print('i é 5')
        continue

    if i == 7:
        print('i é 7')
        break
    
    for j in range(1, 3):
        print(i, j)
else:
    print('acabou')