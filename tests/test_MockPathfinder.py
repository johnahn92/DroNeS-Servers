import json
import os
import unittest
from jsonschema import validate
from Routing.MockPathfinder import MockPathfinder


def load_schema(filename):
    file = os.path.join(os.path.dirname(__file__), "schemas/" + filename)
    with open(file) as f:
        return json.loads(f.read())


class MockPathfinderTest(unittest.TestCase):
    def setUp(self):
        self.payload = MockPathfinder.getRoutes(0)

    def testPayloadSchema(self):
        schema = load_schema("payload.json")
        validate(self.payload, schema)

    def testDroneRouteSchema(self):
        for drone_route in self.payload["drone_routes"]:
            validate(drone_route, load_schema("route.json"))

    def testWaypointSchema(self):
        for drone_route in self.payload["drone_routes"]:
            for waypoint in drone_route["waypoints"]:
                validate(waypoint, load_schema("waypoint.json"))


if __name__ == "__main__":
    unittest.main()
