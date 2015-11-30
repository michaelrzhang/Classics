import numpy as np
from sklearn import svm

# Generate some test data to see how good logistic regression is
# data = [(np.random.rand() + 10, np.random.rand() + 50) for i in range(10)]
# data += [(np.random.rand(), np.random.rand() + 60) for i in range(10)]
# data += [(np.random.rand() - 10 , np.random.rand() + 60) for i in range(10)]
# classified = [0 for i in range(10)]
# classified += [1 for i in range(10)]
# classified += [2 for i in range(10)]


import unittest

class regressionTest(unittest.TestCase):               
    def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

    def test_svm(self):
        clf = svm.SVC()
        data = [(np.random.rand() + 10, np.random.rand() + 50) for i in range(5)]
        data += [(np.random.rand(), np.random.rand() + 60) for i in range(10)]
        data += [(np.random.rand() - 10 , np.random.rand() + 60) for i in range(10)]
        classified = [0 for i in range(5)]
        classified += [1 for i in range(10)]
        classified += [2 for i in range(10)]
        clf.fit(data, classified)
        self.assertEqual(clf.predict([[10, 51]]), np.array([0]))
        self.assertEqual(clf.predict([[0, 60]]), np.array([1]))
        self.assertEqual(clf.predict([[-8, 60]]), np.array([2]))


       

if __name__ == '__main__':
    unittest.main()