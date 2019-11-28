from unittest import TestCase
from Simulator import *
import numpy as np


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        world = self.sim.world

        midx = world.width // 2
        midy = world.height // 2

        """ Check with less than two neighbours """
        sim1 = Simulator()
        w1 = sim1.world
        w1.set(midx, midy, 1)

        self.assertEqual(np.sum(sim1.update().world), 0)

        """ Check with more than three neighbours """
        sim2 = Simulator()
        w2 = sim2.world

        ## Set all cells to alive
        for y in range(0, w2.height):
            for x in range(0, w2.width):
                w2.set(x, y, 1)

        self.assertLess(np.sum(sim2.update().world), 4)


    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)
