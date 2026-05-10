from random import randint
class Stoh_grad:
    def __init__(self, data):
        self.a = 0.01 # шаг
        self.e = 0.003 # условие остановки
        self.l = 0.05 # параметр забывания
        self.price = data[0] # результат
        self.data = data[1:] # факторы
        self.b = [0.1, 0.2, 0.2, -0.05] # начальное приближение
        self.y = self.count_y() # теоретический результат
        self.t = 1
        self.b2 = self.count_b2()
        s = randint(1, len(self.price))
        self.Q = ([1 / s * sum([(self.price[i] - self.y[i]) ** 2 for i in range(s)]) +
                  self.t / 2 * self.b2]) # функция ошибки

    def start(self): # запускает алгоритм
        k = randint(0, len(self.price) - 1)
        Qk = self.count_Qk(k)
        self.b = self.upgrade_bk(k)
        self.y = self.count_y()
        # self.Q.append((1 - self.l) * self.Q[-1] - self.b2 + self.l * Qk + self.b2)
        self.Q.append(self.Q[-1] - self.l * self.count_nabl(k))
        self.b2 = self.count_b2()
        if abs(self.Q[-1] - self.Q[-2]) < self.e:
            self.start()
        else:
            print("Ошибка", sum([(self.price[i] - self.y[i]) ** 2 for i in range(len(self.price))]) / len(self.price))
            print("Q[-1]", self.Q[-1])
            print("Q[0]", self.Q[0])
        return self.b

    def count_y(self): # вычисляет значение y теоретического
        y = []
        for i in range(len(self.price)):
            s = 0
            for j in range(len(self.b)):
                s = s + self.b[j] * self.data[j][i]
            y.append(s)
        return y

    def count_Qk(self, k): # вычисляет квадрат ошибки k-го элемента
        Qk = ((self.price[k] - self.y[k]) ** 2)
        return Qk

    def upgrade_bk(self, k): # обновляет вектор b
        nabl = [2 * self.b[i] * self.data[i][k] + self.t * self.b[i] for i in range(len(self.b))] # вычисление градиента
        b = []
        for i in range(len(self.b)):
            b.append(self.b[i] - self.a * nabl[i])
        # print(b[1])
        return b

    def count_b2(self): # функция ошибки
        return sum([b ** 2 for b in self.b])

    def count_nabl(self, k):
        s = 0
        for i in range(len(self.b)):
            s = s + 2 * self.data[i][k] * self.b[i] + self.t * self.b[i]
        return s

# 2<