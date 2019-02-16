from abc import ABC, abstractmethod


class CostFunction(ABC):
    def __init__(self, reward, penalty):
        self.reward = reward
        self.penalty = - penalty

    @abstractmethod
    def getReward(self, elapsed_time):
        pass


class NaiveCostFunction(CostFunction):
    def __init__(self, reward, penalty, valid_time):
        self.valid_time = valid_time
        super(NaiveCostFunction, self).__init__(reward, penalty)

    def getReward(self, elapsed_time):
        if elapsed_time <= self.valid_time:
            return self.reward
        else:
            return self.penalty
