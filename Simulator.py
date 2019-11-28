from World import *
import numpy as np

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None, birth = [3], survival = [2, 3], age=1):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        self.birth = birth
        self.survival = survival
        self.age = age

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

        birth = self.birth  # Birth neighbours
        survival = self.survival # Survival neighbours

        bc = set(range(2, self.age - 1))

        next_generation = World(self.world.width, self.world.height)
        for y in range(self.world.height):
            for x in range(self.world.width):
                lives = self.world.get(x, y)
                neighbours = self.world.get_neighbours(x, y)
                neighbours_count = len([n for n in neighbours if n > 0])

                # Cell dies if it has less than 2 neighbours
                if lives > 0 and neighbours_count not in survival:
                    next_generation.set(x, y, lives-1)
                else:
                    next_generation.set(x, y, lives)

                # Cell birth
                meetsBc = list(set(neighbours) & bc)
                if not lives and neighbours_count in birth:
                    if self.age > 1 and len(meetsBc) > 0:
                        # If there's an age greater than 1, then set the age of the cell to the max age.
                        next_generation.set(x, y, self.age)
                    elif self.age==1:
                        # GOL with out age
                        next_generation.set(x, y, 1)


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

