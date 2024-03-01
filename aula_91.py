def create_multiplier(mult):
    def multiplier(num):
        return num * mult
    return multiplier

duplicate = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)
print(duplicate(2))
print(triple(2))
print(quadruple(2))


