from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION=True

if __name__ == "__main__":
    w = World(110)
    birth = [3, 6]
    survival = [2, 3]

    midX = w.width // 2
    midY = w.height // 2

    w.set(midX - 1, midY, 5)
    w.set(midX + 1, midY, 5)
    w.set(midX - 1, midY - 1, 5)

    sim = Simulator(w, birth, survival, age=6)


    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)