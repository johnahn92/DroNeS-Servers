import json
from json import JSONEncoder


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class StaticObstacle:
    def __init__(self, position, size):
        self.position = Vector3(position)
        self.size = Vector3(size)


class Vector3:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]


class Drone:
    def __init__(self, id, active, position, pick_up, destination):
        self.id = id
        self.active = active
        self.position = Vector3(position)
        self.pick_up = Vector3(pick_up)
        self.destination = Vector3(destination)


class Simulation:
    def __init__(self):
        self.static_obstacles = []
        self.drones = []

    @staticmethod
    def getGeneric():
        sim = Simulation()
        # add some obstacles
        sim.static_obstacles.append(
            StaticObstacle([5, 10, 5], [1, 1, 1]))
        sim.static_obstacles.append(
            StaticObstacle([10, 10, 10], [1, 1, 1]))
        sim.static_obstacles.append(
            StaticObstacle([15, 10, 15], [1, 1, 1]))
        # add some drones
        sim.drones.append(
            Drone(1, False, [0, 0, 0], [6, 5, 7], [1, 3, 7]))
        sim.drones.append(
            Drone(2, True, [2, 2, 2], [12, 5, 16], [7, 5, 13]))
        return json.dumps(sim, cls=Encoder)

    @staticmethod
    def getNoActiveDrones():
        sim = Simulation()
        # add some obstacles
        sim.static_obstacles.append(
            StaticObstacle([5, 10, 5], [1, 1, 1]))
        sim.static_obstacles.append(
            StaticObstacle([10, 10, 10], [1, 1, 1]))
        sim.static_obstacles.append(
            StaticObstacle([15, 10, 15], [1, 1, 1]))
        # add some drones
        sim.drones.append(
            Drone(1, False, [0, 0, 0], [6, 5, 7], [1, 3, 7]))
        sim.drones.append(
            Drone(2, False, [2, 2, 2], [12, 5, 16], [7, 5, 13]))
        return json.dumps(sim, cls=Encoder)
