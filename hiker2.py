from typing import Callable
from dataclasses import dataclass


@dataclass(slots=True)
class Node:
    state: object
    system: object
    unvisited: list


@dataclass(slots=True, frozen=True)
class Hiker:
    goto: Callable
    choices: Callable

    def __call__(self, obj, matching: Callable[[...], bool], start) -> list[list]:
        output = []  # Definire uno spazio per i risultati.
        system = self.goto(obj, start)  # Definire il sistema di partenza.
        unvisited = self.choices(system)  # Definire gli stati non ancora visitati.
        stack = [Node(start, system, unvisited)]  # Definire una pila di dati.
        while stack:  # Mentre la pila non e' vuota
            head = stack[-1]  # si accede ai dati in cima.
            print([_.state for _ in stack], [_.unvisited for _ in stack])  # Disegnare sul display dei dati (non necessario).
            if not head.unvisited:  # Se tutti gli stati in cima alla pila sono stati visitati
                del stack[-1]  # rimuovere questi dati e
                continue  # riaccedere alla nuova cima della pila.
            _state = head.unvisited.pop()  # Accedere ad uno dei prossimi stati visitabili (visitandoli).
            _system = self.goto(head.system, _state)  # Definire il sistema associato allo stato visitato.
            stack.append(Node(_state, _system, self.choices(_system)))  # Aggiungere alla pila questi dati.
            if matching(_system):  # Se il sistema ha delle proprieta' desiderate.
                output.append([item.state for item in stack])  # si aggiunge il cammino degli stati percorsi fino ad ora ai risultati.
        return output  # Finita la pila dei dati si riportano i risultati ottenuti.


if __name__ == "__main__":

    MAZE = {'A': {'B': {'D': {'G': False, 'H': {'J': {'M': True}}}, 'E': True}, 'C': False}}

    hiker = Hiker(
        lambda d, k: d[k],
        lambda obj: list(range(len(obj))) if isinstance(obj, list)
        else (list(obj.keys()) if isinstance(obj, dict)
              else list())
    )

    print(hiker(MAZE, lambda v: type(v) == bool and bool(v), 'A'))
