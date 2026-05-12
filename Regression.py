from random import randint
class Regression:
    def __init__(self, data, b, a=0.000006, l=0.1, e=0.001):
        self.a = a # шаг
        self.l = l # параметр забывания
        self.e = e  # условие остановки
        self.t = 0.5 # коэффициент регуляризации
        self.b = b # начальное приближение
        self.data = data[1:]
        self.y_pr = data[0]
        self.Q = [self.count_Q0() + self.t / 2 * sum([el ** 2 for el in self.b])] # функция ошибки

    def count_y_th(self, k):
        y_th = 0
        for i in range(len(self.data)):
            y_th = y_th + self.b[i] * self.data[i][k]
        return y_th

    def count_Q0(self):
        S = 30
        k = []
        for i in range(S):
            el = randint(0, len(self.y_pr) - 1)
            while el in k:
                el = randint(0, len(self.y_pr) - 1)
            k.append(el)
        arr = [(self.y_pr[i] - self.count_y_th(i)) ** 2 for i in k]
        return sum(arr) / S

    def count_Qk(self, k):
        return (self.y_pr[k] - self.count_y_th(k)) ** 2

    def upgrade_b(self, grad):
        return [self.b[i] - self.a * grad[i] for i in range(len(self.b))]

    def upgrade_Q(self, Qk):
        return (1 - self.l) * self.Q[-1] + self.l * Qk

    def grad(self, k):
        return [-2 * self.data[i][k] * (self.y_pr[k] - self.count_y_th(k)) + self.b[i] * self.t
                for i in range(len(self.b))]

    def start_alg(self):
        k = randint(0, len(self.y_pr) - 1)
        grad = self.grad(k)
        Qk = self.count_Qk(k)
        self.b = self.upgrade_b(grad)
        self.Q.append(self.upgrade_Q(Qk))
        delta = abs(self.Q[-1] - self.Q[-2])
        while delta > self.e:
            k = randint(0, len(self.y_pr) - 1)
            grad = self.grad(k)
            Qk = self.count_Qk(k)
            self.b = self.upgrade_b(grad)
            self.Q.append(self.upgrade_Q(Qk))
            delta = abs(self.Q[-1] - self.Q[-2])
        return self.b

    def sko(self):
        Q = [(self.y_pr[i] - self.count_y_th(i)) ** 2 for i in range(len(self.y_pr))]
        sko = (sum(Q) / len(Q)) ** 0.5
        return sko