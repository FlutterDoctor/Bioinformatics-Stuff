import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=1000):
        self.lr = lr
        self.num_iter = num_iter

    def fit(self, X, y):
        self.theta = np.zeros(X.shape[1])
        for _ in range(self.num_iter):
            z = np.dot(X, self.theta)
            h = self._sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / y.size
            self.theta -= self.lr * gradient

    def predict_prob(self, X):
        return self._sigmoid(np.dot(X, self.theta))

    def predict(self, X):
        return self.predict_prob(X).round()

    @staticmethod
    def _sigmoid(z):
        return 1 / (1 + np.exp(-z))
