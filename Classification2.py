from random import randint
from math import exp
class Classification:
    def __init__(self, data, b, a=0.0000000001, l=0.1, e=0.001):
        self.a = a # шаг
        self.l = l # параметр забывания
        self.e = e  # условие остановки
        self.t = 0.1 # коэффициент регуляризации
        self.b = b # начальное приближение
        self.data = data[1:]
        self.y_pr = data[0]
        self.Q = [self.count_Q0() + self.t / 2 * sum([el ** 2 for el in self.b])] # функция ошибки

    def count_y_th(self, k):
        if self.count_Qk(k) > 0.5:
            return True
        return False

    def count_Q0(self):
        S = 30
        k = []
        while len(k) < S:
            el = randint(0, len(self.y_pr) - 1)
            if el not in k:
                k.append(el)
        p = 0
        for el in k:
            arr = [self.data[i][el] * self.b[i] for i in range(len(self.b))]
            p = p + 1 / (1 + exp(sum(arr) * self.y_pr[el]))
        return p

    def count_Qk(self, k):
        arr = [self.data[i][k] * self.b[i] for i in range(len(self.b))]
        return 1 / (1 + exp(sum(arr) * self.y_pr[k]))

    def upgrade_b(self, grad):
        return [self.b[i] - self.a * grad[i] for i in range(len(self.b))]

    def upgrade_Q(self, Qk):
        return (1 - self.l) * self.Q[-1] + self.l * Qk

    def grad(self, k):
        grade = sum([self.data[i][k] * self.b[i] for i in range(len(self.b))]) * self.y_pr[k]
        res = grade * exp(grade - 1) / (1 + exp(grade)) ** 2
        return [self.data[i][k] * res for i in range(len(self.b))]

    def start_alg(self):
        k = randint(0, len(self.y_pr) - 1)
        grad = self.grad(k)
        Qk = self.count_Qk(k)
        self.b = self.upgrade_b(grad)
        self.Q.append(self.upgrade_Q(Qk))
        delta = abs(self.Q[-1] - self.Q[-2])
        x = self.tr()
        while (delta > self.e or x[0] <= 2 * x[1]) and len(self.Q) < 100:
            k = randint(0, len(self.y_pr) - 1)
            grad = self.grad(k)
            Qk = self.count_Qk(k)
            self.b = self.upgrade_b(grad)
            self.Q.append(self.upgrade_Q(Qk))
            delta = abs(self.Q[-1] - self.Q[-2])
            x = self.tr()
        print(len(self.Q))
        print(x[0], x[1])
        print(delta > self.e or x[0] <= x[1])
        return self.b

    def sko(self):
        Q = [(self.y_pr[i] - self.count_y_th(i)) ** 2 for i in range(len(self.y_pr))]
        sko = (sum(Q) / len(Q)) ** 0.5
        return sko

    def tr(self):
        y_th = []
        for i in range(len(self.y_pr)):
            y_th.append(self.count_y_th(i) == self.y_pr[i])
        return [y_th.count(True), y_th.count(False)]