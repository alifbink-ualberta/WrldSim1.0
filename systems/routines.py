def get_routine_location(person):

    routines = {

        "Farmer": [
            "Farm",
            "Market",
            "Home"
        ],

        "Merchant": [
            "Market",
            "Tavern",
            "Home"
        ],

        "Hunter": [
            "Forest",
            "Market",
            "Tavern",
            "Home"
        ],

        "Scholar": [
            "Library",
            "Market",
            "Home"
        ],

        "Blacksmith": [
            "Workshop",
            "Market",
            "Tavern",
            "Home"
        ]
    }

    return routines.get(
        person.occupation,
        ["Home"]
    )