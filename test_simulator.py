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

        """ Ressurect the cell if it has exactly three neighbours and was previously dead  """
        sim3 = Simulator()
        w3 = sim3.world

        midX = w3.width // 2
        midY = w3.height // 2

        w3.set(midX - 1, midY + 1, 1)
        w3.set(midX - 1, midY - 1, 1)
        w3.set(midX - 1, midY, 1)
        w3.set(midX - 1, midY + 2, 1)

        # print(w3)
        new_world = sim3.update()
        self.assertGreater(np.sum(new_world.world), 3)

        """PART 2"""
        birth = [3, 6]
        survival = [2, 3]

        """ Check with less than two neighbours, with new rules """
        sim4 = Simulator(birth=birth, survival=survival)
        w4 = sim4.world
        w4.set(midx, midy, 1)

        self.assertEqual(np.sum(sim4.update().world), 0)

        """ Check with more than three neighbours, with new rules """
        sim5 = Simulator(birth=birth, survival=survival)
        w5 = sim5.world

        ## Set all cells to alive
        for y in range(0, w5.height):
            for x in range(0, w5.width):
                w5.set(x, y, 1)

        self.assertLess(np.sum(sim5.update().world), 4)

        """ Ressurect the cell if it has 6 neighbours  """
        sim6 = Simulator(birth=birth, survival=survival)
        w6 = sim6.world

        midX = w6.width // 2
        midY = w6.height // 2

        w6.set(midX - 1, midY + 1, 1)
        w6.set(midX - 1, midY - 1, 1)
        w6.set(midX - 1, midY, 1)
        w6.set(midX, midY + 1, 1)
        w6.set(midX, midY - 1, 1)
        w6.set(midX + 1, midY, 1)

        new_world = sim6.update()
        self.assertGreater(np.sum(new_world.world), 6)



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
