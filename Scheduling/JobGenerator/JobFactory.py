import configparser
import random
import time

from CostFunction import NaiveCostFunction


class Job:
    def __init__(self):
        self.uid = None
        self.creation_time = None
        self.content = None
        self.cost_function = None
        self.pick_up = None
        self.destination = None


class JobFactory:
    def __init__(self, origin, dispatch_range):
        self.origin = origin
        self.range = dispatch_range
        self.counter = 0
        self.items = []
        self.getConfig()

    def getConfig(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        for (item, params) in config['Jobs'].items():
            entry = {'item': item,
                     'reward': eval(params)[0],
                     'penalty': eval(params)[1],
                     'valid_for': eval(params)[2]}
            self.items.append(entry)

    def generateJob(self):
        # Job creation
        job = Job()
        job.uid = self.generateUID()
        job.creation_time = int(time.time())
        # Assigning item to job
        item = self.getRandomItem()
        job.content = item['item']
        # Assigning cost function
        reward = random.randint(item['reward'][0], item['reward'][1])
        penalty = random.randint(item['penalty'][0], item['penalty'][1])
        valid_for = random.randint(item['valid_for'][0], item['valid_for'][1])
        job.cost_function = NaiveCostFunction(reward, penalty, valid_for)
        return job.__dict__

    # Ignores the given probability of the job, and picks one at random
    def getRandomItem(self):
        return random.choice(self.items)

    def generateUID(self):
        self.counter += 1
        return self.counter
