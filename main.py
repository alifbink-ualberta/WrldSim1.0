from simulation.world import World


def main():

    world = World()

    world.setup()

    print()
    print("================================")
    print("       WORLD SIMULATION")
    print("================================")
    print()

    print(
        f"Population: {len(world.people)}"
    )

    print()
    print("Beginning simulation...")
    print()

    world.run(days=30)

    print()
    print("================================")
    print("       SIMULATION COMPLETE")
    print("================================")


if __name__ == "__main__":
    main()