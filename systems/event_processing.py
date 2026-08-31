# systems/event_processing.py


def process_event(event):

    for person in event.participants:

        experience_event(
            person,
            event
        )


def experience_event(person, event):

    from simulation.experience import Experience

    experience = Experience(
        person=person,
        event_type=event.event_type,
        description=event.description,
        participants=event.participants,
        intensity=event.significance
    )

    person.remember(
        experience
    )