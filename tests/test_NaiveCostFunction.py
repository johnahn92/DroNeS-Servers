import unittest
from Scheduling.CostFunction import NaiveCostFunction


class NaiveCostFunctionTest(unittest.TestCase):
    def setUp(self):
        self.reward = 5
        self.penalty = 10
        self.valid_time = 15
        self.cf = NaiveCostFunction(self.reward, self.penalty, self.valid_time)

    def testInitialisation(self):
        self.assertEqual(self.cf.reward, self.reward)
        self.assertEqual(self.cf.penalty, -self.penalty)
        self.assertEqual(self.cf.valid_time, self.valid_time)

    def testGetReward(self):
        # initial reward should be just the reward
        self.assertEqual(self.cf.getReward(0), self.reward)
        # reward before valid_time should also be reward
        self.assertEqual(self.cf.getReward(10), self.reward)
        # reward on the valid_time should also be reward
        self.assertEqual(self.cf.getReward(15), self.reward)
        # reward after valid_time should be (negative of) penalty
        self.assertEqual(self.cf.getReward(20), -self.penalty)


if __name__ == '__main__':
    unittest.main()
