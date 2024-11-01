from dataclasses import dataclass, field
from typing import Any, Hashable, Callable



def hiker(maze: dict, start: str) -> list[list[str]]:
    output = []
    path = [start]
    space = [maze[start]]
    plan = [[door for door in space[-1]]]
    while plan:
        print("path:", path)
        print("plan:", plan, '\n')
        for door in plan[-1]:
            room = space[-1][door]
            if isinstance(room, dict):
                plan[-1].remove(door)
                path.append(door)
                space.append(room)
                plan.append(list(room.keys()))
                break
            elif isinstance(room, bool):
                if room == True:
                    plan[-1] = []
                    output.append(path.copy() + [door])
                elif room == False:
                    plan[-1].remove(door)
                while True:
                    if plan and plan[-1] == []:
                        del plan[-1]
                        del space[-1]
                        del path[-1]
                    else:
                        break
    return output


if __name__ == "__main__":

    MAZE = {'A': {'B': {'D': {'G': False, 'H': {'J': {'M': True}}}, 'E': True}, 'C': False}}
    print(hiker(MAZE, 'A'))
