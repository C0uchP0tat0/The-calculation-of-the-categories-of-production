class Rkp():
    add=[]

    def __init__(self, name, quantity, warmth):
        self.name = name
        self.quantity = quantity
        self.warmth = warmth
        
    def adds(self):
        self.add.append(self.quantity * self.warmth)

    def relative(square):
        load = sum(Rkp.add)/square
        return '[Удельная пожарная нагрузка - %s МДж/кв.м]' % load

    def __repr__(self):
        return '[Материал - %s, Количество материала - %s кг, \
Теплота сгорания - %s МДж/кг]' % (self.name, self.quantity, self.warmth)

if __name__ == '__main__':
    wood = Rkp('Древесина', 10, 13.4)
    silk = Rkp('Хлопок', 10, 14)
    rubber = Rkp('Резина', 10, 14)
    print(wood, silk, rubber)
    wood.adds()
    silk.adds()
    rubber.adds()
    #print(Rkp.add)
    #print(sum(Rkp.add))
    print(Rkp.relative(20))




