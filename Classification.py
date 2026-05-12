from random import randint
from math import exp


class Classification:

    def __init__(self, data, b, a=0.01, l=0.1, e=0.001,    t=0.1):
        self.a = a
        self.l = l
        self.e = e
        self.t = t
        self.b = b
        self.data = data[1:]
        self.y_pr = data[0]

        self.Q = [self.count_Q0()]

    # -----------------------------
    # sigmoid
    # -----------------------------
    def sigmoid(self, z):
        return 1 / (1 + exp(-z))

    # -----------------------------
    # линейная комбинация
    # -----------------------------
    def linear(self, k):
        return sum(
            self.data[i][k] * self.b[i]
            for i in range(len(self.b))
        )

    # -----------------------------
    # вероятность класса
    # -----------------------------
    def predict_proba(self, k):
        return self.sigmoid(self.linear(k))

    # -----------------------------
    # предсказанный класс
    # -----------------------------
    def count_y_th(self, k):

        p = self.predict_proba(k)

        if p >= 0.5:
            return 1

        return -1

    # -----------------------------
    # logistic loss для одного объекта
    # -----------------------------
    def count_Qk(self, k):

        z = self.linear(k)
        y = self.y_pr[k]

        return 1 / (1 + exp(y * z))

    # -----------------------------
    # начальная ошибка
    # -----------------------------
    def count_Q0(self):

        S = min(30, len(self.y_pr))

        idx = []

        while len(idx) < S:

            el = randint(0, len(self.y_pr) - 1)

            if el not in idx:
                idx.append(el)

        q = 0

        for k in idx:
            q += self.count_Qk(k)

        q /= S

        # L2-регуляризация
        q += self.t / 2 * sum(w ** 2 for w in self.b)

        return q

    # -----------------------------
    # градиент
    # -----------------------------
    def grad(self, k):

        z = self.linear(k)
        y = self.y_pr[k]

        coef = -y / (1 + exp(y * z))

        grad = []

        for i in range(len(self.b)):

            g = self.data[i][k] * coef

            # регуляризация
            g += self.t * self.b[i]

            grad.append(g)

        return grad

    # -----------------------------
    # обновление весов
    # -----------------------------
    def upgrade_b(self, grad):

        return [
            self.b[i] - self.a * grad[i]
            for i in range(len(self.b))
        ]

    # -----------------------------
    # обновление функционала качества
    # -----------------------------
    def upgrade_Q(self, Qk):

        return (1 - self.l) * self.Q[-1] + self.l * Qk

    # -----------------------------
    # обучение
    # -----------------------------
    def start_alg(self, max_iter=1000):

        delta = 1e9
        iteration = 0

        while delta > self.e and iteration < max_iter:

            k = randint(0, len(self.y_pr) - 1)

            grad = self.grad(k)

            self.b = self.upgrade_b(grad)

            Qk = self.count_Qk(k)

            self.Q.append(self.upgrade_Q(Qk))

            delta = abs(self.Q[-1] - self.Q[-2])

            iteration += 1

        print("iterations =", iteration)
        print("Q =", self.Q[-1])

        return self.b

    # -----------------------------
    # accuracy
    # -----------------------------
    def tr(self):

        correct = 0

        for i in range(len(self.y_pr)):

            if self.count_y_th(i) == self.y_pr[i]:
                correct += 1

        return correct, len(self.y_pr) - correct