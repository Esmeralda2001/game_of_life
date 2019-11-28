from World import *
import numpy as np

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        #TODO: Do something to evolve the generation

        next_generation = World(self.world.width, self.world.height)
        for y in range(self.world.height):
            for x in range(self.world.width):
                cell_alive = self.world.get(x, y)
                neighbours = sum(self.world.get_neighbours(x, y))

                # Cell dies if it has less than 2 neighbours
                if cell_alive and neighbours < 2:
                    next_generation.set(x, y, 0)
                elif cell_alive and neighbours > 3:
                    next_generation.set(x, y, 0)
                else:
                    next_generation.set(x, y, cell_alive)


        self.set_world(next_generation)


        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world

