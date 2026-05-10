from random import randint
class Stoh_grad2:
    def __init__(self, data, b):
        self.y_pr = data[0] # практическое значение результата
        self.data = data[1:] # значения факторов
        self.l = 0.1 # параметр забывания
        self.a = 0.01 # шаг
        self.e = 0.0001 # условие остановки
        self.b = b # начальное приближение
        self.t = 1
        self.y_th = self.count_y_th() # теоретическое значение результата
        self.k = []
        # S = randint(1, int(len(self.data[0]) / 4))
        S = 30
        for i in range(S):
            k = randint(0, len(self.y_pr) - 1)
            while k in self.k:
                k = randint(0, len(self.y_pr) - 1)
            self.k.append(k)
        Q = 0
        for el in self.k:
            Q += (self.count_qk(el))
        self.Q = [Q / S]
        # self.Q = [1000000]
        # self.Q = [sum([self.count_qk(k) for k in range(S)]) / S]

    def start(self):
        k = randint(0, len(self.data[0]) - 1)
        while k in self.k:
            k = randint(0, len(self.data[0]) - 1)
        self.Q.append(self.upgrade_qk(k))
        if (abs(self.Q[-2] - self.Q[-1]) > self.e or len(self.Q) <= 2) and len(self.Q) < 250:
            self.upgrade_b(k)
            self.y_th = self.count_y_th()
            print(len(self.Q))
            self.start()
        else:
            print(len(self.Q) - 1)
            print(self.Q[-1] ** 0.5)
            # print(self.sko())
            # Qпосл < Qпредпоследнее + e
        return self.b

    def count_y_th(self):
        y_th = [0 for i in range(len(self.data[1]))]
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                y_th[j] = y_th[j] + self.data[i][j] * self.b[i] + self.t / 2 * self.b[i] ** 2
        return y_th

    def count_qk(self, k):
        return (self.y_pr[k] - self.y_th[k]) ** 2

    def upgrade_b(self, k):
        grad = self.count_grad(k)
        for i in range(len(self.b)):
            self.b[i] = self.b[i] - self.a * grad[i]

    def count_grad(self, k):
        # return [2 * self.b[i] * self.data[i][k] for i in range(len(self.b))]
        return [2 * self.data[i][k] * (self.y_th[k] - self.y_pr[k]) + self.t * self.b[i]
                for i in range(len(self.data))]

    def upgrade_qk(self, k):
        return (1 - self.l) * self.Q[-1] + self.l * self.count_qk(k)

    def sko(self):
        return (sum([(self.y_pr[i] - self.y_th[i]) ** 2 for i in range(len(self.y_pr))]) / len(self.y_pr)) ** 0.5
