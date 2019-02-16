import configparser
import math
import random
import time

from CostFunction import NaiveCostFunction

EARTH_RADIUS = 6371  # km
# 1 degree latitute in meters
ONE_DEGREE = EARTH_RADIUS * 2 * math.pi / 360 * 1000


def randomPointOnDisk(radius):
    r = radius * random.uniform(0, 1)
    theta = random.uniform(0, 1) * 2 * math.pi
    return (r * math.cos(theta), r * math.sin(theta))


def randomCoords(lat, lon, radius):
    dx, dy = randomPointOnDisk(radius)
    random_lat = lat + (dy / ONE_DEGREE)
    random_lon = lon + (dx / (ONE_DEGREE * math.cos(lat * math.pi / 180)))
    return (random_lat, random_lon)


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
        # Assigning pick_up and destination
        job.pick_up = randomCoords(self.origin[0], self.origin[1], self.range)
        job.destination = randomCoords(self.origin[0], self.origin[1],
                                       self.range)
        return job.__dict__

    # Ignores the given probability of the job, and picks one at random
    def getRandomItem(self):
        return random.choice(self.items)

    def generateUID(self):
        self.counter += 1
        return self.counter
