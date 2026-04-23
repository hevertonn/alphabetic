import sys


class Automaton:
    __states = {}
    __alphabet = []

    def __init__(self, num_states, alphabet):
        for i in range(num_states):
            self.__states[f"q{i + 1}"] = []

        if type(alphabet) is list:
            self.__alphabet = alphabet
        elif type(alphabet) is str:
            token = ""

            for c in alphabet:
                if c != "," and c != "\n":
                    token += c
                else:
                    self.__alphabet.append(token)
                    token = ""

    def set_transition(self, qi, qj, character):
        if qi not in self.__states.keys() or qj not in self.__states.keys():
            print(f"Estados {qi} e {qj} não pertencem ao autômato")
            return

        if character not in self.__alphabet:
            print(f"Caractere {character} não pertence ao alfabeto do autômato")
            return

        self.__states[qi].append((character, qj))

    def get_states(self):
        return self.__states.keys()

    def get_alphabet(self):
        return self.__alphabet

    def string(self):
        automaton_str = ""

        for state, transactions in self.__states.items():
            automaton_str += state + ":\n    "

            for t in transactions:
                automaton_str += f"δ({state}, {t[0]}) = {t[1]}  "

            automaton_str += "\n"

        return automaton_str


def scan_automaton():
    num_states = int(input("Digite o número de estados do autômato: "))
    print()

    print("Digite os caracteres do alfabeto separados por vírgula:\n    ", end="")
    automaton = Automaton(num_states, sys.stdin.readline())
    print()

    print("Defina as transições correspondentes:")

    for i in automaton.get_states():
        for j in automaton.get_alphabet():
            automaton.set_transition(i, input(f"    δ({i}, {j}) = "), j)
    print()

    return automaton
