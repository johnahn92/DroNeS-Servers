class Jsonable:
    def json(self):
        return self.__dict__


class StaticObstacle(Jsonable):
    def __init__(self, position, size):
        self.position = Vector3(position).json()
        self.size = Vector3(size).json()


class Vector3(Jsonable):
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]


class Drone(Jsonable):
    def __init__(self, id, active, position, pick_up, destination):
        self.id = id
        self.active = active
        self.position = Vector3(position).json()
        self.pick_up = Vector3(pick_up).json()
        self.destination = Vector3(destination).json()


class Simulation(Jsonable):
    def __init__(self):
        self.static_obstacles = []
        self.drones = []

    @staticmethod
    def getGeneric():
        sim = Simulation()
        # add some obstacles
        sim.static_obstacles.append(
            StaticObstacle([5, 10, 5], [1, 1, 1]).json())
        sim.static_obstacles.append(
            StaticObstacle([10, 10, 10], [1, 1, 1]).json())
        sim.static_obstacles.append(
            StaticObstacle([15, 10, 15], [1, 1, 1]).json())
        # add some drones
        sim.drones.append(
            Drone(1, False, [0, 0, 0], [6, 5, 7], [1, 3, 7]).json())
        sim.drones.append(
            Drone(2, True, [2, 2, 2], [12, 5, 16], [7, 5, 13]).json())
        return sim.json()

    @staticmethod
    def getNoActiveDrones():
        sim = Simulation()
        # add some obstacles
        sim.static_obstacles.append(
            StaticObstacle([5, 10, 5], [1, 1, 1]).json())
        sim.static_obstacles.append(
            StaticObstacle([10, 10, 10], [1, 1, 1]).json())
        sim.static_obstacles.append(
            StaticObstacle([15, 10, 15], [1, 1, 1]).json())
        # add some drones
        sim.drones.append(
            Drone(1, False, [0, 0, 0], [6, 5, 7], [1, 3, 7]).json())
        sim.drones.append(
            Drone(2, False, [2, 2, 2], [12, 5, 16], [7, 5, 13]).json())
        return sim.json()
