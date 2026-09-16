
import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["Bob", "Alice", "Dylan", "Charlie"]
    actions: list[str] = ["run", "grab", "move", "eat", "sleep", "release"]
    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def remove_event(events: list[tuple[str, str]]
                 ) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event: tuple[str, str] = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    gen: typing.Generator[tuple[str, str], None, None] = gen_event()

    for i in range(1, 1001):
        print(f"Action {i}: {next(gen)}")
    events: list = list()
    for i in range(1, 11):
        events.append(next(gen))
    print(f"Built list with 10 events: {events}")
    for event in remove_event(events):
        print(f"Got event {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
