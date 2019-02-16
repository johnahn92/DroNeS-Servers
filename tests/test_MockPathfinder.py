import unittest
from Routing.MockPathfinder import MockPathfinder


class MockPathfinderTest(unittest.TestCase):
    def setUp(self):
        self.mock_payload = MockPathfinder.getRoutes(0)

    def testPayloadFormat(self):
        self.assertTrue('drone_routes' in self.mock_payload)
        self.assertTrue('timestamp' in self.mock_payload)
        self.assertTrue(type(self.mock_payload['drone_routes']) is list)

    def testPayloadTypes(self):
        self.assertIs(type(self.mock_payload), dict)
        self.assertIs(type(self.mock_payload['timestamp']), int)
        self.assertIs(type(self.mock_payload['drone_routes']), list)

    def testRouteFormat(self):
        self.mock_route = self.mock_payload['drone_routes'][0]
        self.assertTrue('waypoints' in self.mock_route)
        self.assertTrue('drone_id' in self.mock_route)

    def testRouteTypes(self):
        self.mock_route = self.mock_payload['drone_routes'][0]
        self.assertIs(type(self.mock_route['waypoints']), list)
        self.assertIs(type(self.mock_route['drone_id']), int)

    def testWaypointsFormat(self):
        self.mock_waypoints = self.mock_payload['drone_routes'][0]['waypoints']
        self.assertTrue('x' in self.mock_waypoints[0])
        self.assertTrue('y' in self.mock_waypoints[0])
        self.assertTrue('z' in self.mock_waypoints[0])

    def testWaypointsTypes(self):
        self.mock_waypoints = self.mock_payload['drone_routes'][0]['waypoints']
        self.assertIs(type(self.mock_waypoints[0]['x']), int)
        self.assertIs(type(self.mock_waypoints[0]['y']), int)
        self.assertIs(type(self.mock_waypoints[0]['z']), int)


if __name__ == '__main__':
    unittest.main()
