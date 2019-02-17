from abc import ABC, abstractmethod

'''
Cost functions determine how the reward of a job changes over time. By using an
abstract CostFunction class, different types of cost funtions can be developed
without having to modify the existing code for the Jobs.

Cost functions will receive:

reward - A numeric type defining the initial (and logically the upper bound) of
         the reward for completing the job.

penalty - A numetic type defining the final (and logically the lower bound) of
          the reward for not completing the job.

Since cost functions are not meant to run asynchronously, the responsibility of
"timekeeping" will be done by whoever initialises the job.

Each cost function should imeplement an `getReward(elapsed_time)` method which
returns the reward of the job if completed at <elapsed_time> seconds.
'''


# Simple base class that all other cost functions should inherit from
# The getReward function should be overriden in concrete cost fucntion classes
# Note that we negate the penalty initially for sanity purposes
class CostFunction(ABC):
    def __init__(self, reward, penalty):
        self.reward = reward
        self.penalty = - penalty

    @abstractmethod
    def getReward(self, elapsed_time):
        pass


# A naive piece-wise continious cost function that always returns <reward> if
# completed within <valid_time>, and <penalty> otherwise
class NaiveCostFunction(CostFunction):
    def __init__(self, reward, penalty, valid_time):
        self.type = "naive"
        self.valid_time = valid_time
        super().__init__(reward, penalty)

    def getReward(self, elapsed_time):
        if elapsed_time <= self.valid_time:
            return self.reward
        else:
            return self.penalty
