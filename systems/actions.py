DURATIONS = {

    "eat": 10,

    "sleep": 8 * 60,

    "work": 4 * 60,

    "practice": 2 * 60,

    "socialize": 30,

    "explore": 4 * 60,

    "buy": 15,

    "sell": 15
}


def get_action_duration(action_type):

    return DURATIONS.get(
        action_type,
        10
    )