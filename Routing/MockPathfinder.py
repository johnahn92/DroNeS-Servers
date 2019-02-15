import time
import random


class Payload(object):
    def __init__(self):
        self.drone_routes = []

    def set_time(self):
        self.timestamp = int(time.time())

    def add_drone_route(self, drone_route):
        self.drone_routes.append(drone_route.__dict__)


class DroneRoute(object):
    def __init__(self):
        self.waypoints = []

    def set_drone_id(self, id):
        self.drone_id = id

    def add_waypoint(self, waypoint):
        self.waypoints.append(waypoint.__dict__)


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class MockPathfinder:
    @staticmethod
    def getRoutes(data):
        # create payload
        payload = Payload()
        # create route for one drone
        route = DroneRoute()
        for i in range(3):
            point = Point(random.randint(0, 5), 5, random.randint(0, 5))
            route.add_waypoint(point)
        route.set_drone_id(1)
        # add drone route to payload
        payload.add_drone_route(route)
        payload.set_time()
        return payload.__dict__
