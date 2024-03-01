x = 2

def test():
    # global x
    x = 10
    def test_2():
        x = 59
        y = 35
        print(x, y)
    test_2()
    print(x)
test() 

print(x)