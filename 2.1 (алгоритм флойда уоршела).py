class Evense():   #класс задающий ребро графа
    def _init_(self, a=0, b=0):
        self.cord = [a, b]   # координаты ребра в графе
        self.mass = 2 # вес ребра.

    def isin(self, a):  # проверка приндлежности вершины ребру
        return a in self.cord


class Point():  # класс задающий вершину графа
    def _init_(self, c = 0):
        self.cord = c   #координаты вершины
        self.defect = 0 # булево значение, пройдена ли вершина 1-нет 0-да

    def _getitem_(self):
        return self.cord


class Graph(): # класс задающий граф
    def _init_(self):
        self.points = [] # вершины графа
        self.evenses = [] # ребра графа

    def converttopoint(self, evense): #конвертация ребра графа в кортеж вершин
        u = Point()
        v = Point()
        u._init_(evense.cord[0])
        v._init_(evense.cord[1])
        s = u,  v
        return s

    def converttoevense(self, a, b):  # конвертация 2ух вершин в ребро,
        evense = Evense()
        evense._init_(a.cord, b.cord)
        return evense

    def addevense(self, a=0, b=0): #Добавление ребра, и запись его вершин
        newevense = Evense()
        newevense._init_(a, b)
        c1 = Point()
        c2 = Point()
        c1._init_(newevense.cord[0])
        c2._init_(newevense.cord[1])
        c1.defect = 1
        c2.defect = 1
        self.addpoint(c1)
        self.addpoint(c2)
        if newevense not in self.evenses:
            self.evenses.append(newevense)

    def addpoint(self, c=0): # добавление вершины в граф
        newpoint = Point()
        newpoint._init_(c)
        if newpoint not in self.points:
            self.points.append(newpoint)

    def _get_(self): #преобразование списка вершин в список их номеров
        return [str(i.cord) for i in self.points]